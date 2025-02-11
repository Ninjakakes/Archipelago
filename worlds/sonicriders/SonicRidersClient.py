import asyncio
import traceback
from typing import Optional

import dolphin_memory_engine

import Utils
from BaseClasses import ItemClassification as ItemClass
from CommonClient import get_base_parser, CommonContext, server_loop, gui_enabled, logger, ClientCommandProcessor
from NetUtils import ClientStatus
from worlds.sonicriders.Items import Junk
from .Constants import BASE_ID
from . import Locations, Items, CHR_EGGMAN, GEAR_E_RIDER, CHR_SHADOW, GEAR_DARKNESS, GEAR_DEFAULT, STAGE_ID_TO_NAME, \
    CHR_ID_TO_NAME, GEAR_ID_TO_NAME, CHR_SUPER_SONIC, CHR_SONIC, STAGE_BABYLON_GUARDIAN, GEAR_CHAOS_EMERALD, CHR_WAVE

CONNECTION_REFUSED_GAME_STATUS = (
    "Dolphin failed to connect. Please load a ROM for Sonic Riders. Currently {1}. Trying again in 5 seconds..."
)
CONNECTION_REFUSED_SAVE_STATUS = (
    "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."
)
CONNECTION_LOST_STATUS = (
    "Dolphin connection was lost. Please restart your emulator and make sure Sonic Riders is running."
)

CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."

SONIC_RIDERS_ID = "GXEE8P"


class GAME_ADDRESSES:
    GAME_STATE = 0x803D905C
    SAVED_INDEX = 0x806A9061
    STAGE_ARRAY = 0x806A8D04
    CHR_ARRAY = 0x806A90A0
    GEAR_ARRAY_BOARD = 0x806A9048
    GEAR_ARRAY_BIKE = 0x806A9070
    GEAR_ARRAY_SKATES = 0x806A908E
    RACE_TYPE = 0x806129A0
    CURRENT_STAGE = 0x806129A8
    PLAYER_CHR = 0x806094FA
    PLAYER_GEAR = 0x806094FB
    PLAYER_RINGS = 0x80609FD8
    PLAYER_FINISH_TIME = 0x8060A434
    PLAYER_LAP = 0x8060A46A


class GAME_STATES:
    LOADING = 0
    RACE = [1, 2]
    MAIN_MENU = 13
    STAGE_SELECT = 22


class SonicRidersCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_dolphin(self):
        """Prints the current Dolphin status to the client."""
        if isinstance(self.ctx, SonicRidersContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")


class SonicRidersContext(CommonContext):
    command_processor = SonicRidersCommandProcessor
    game = "Sonic Riders"
    items_handling = 0b111

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.override_settings = []
        self.dolphin_sync_task: Optional[asyncio.Task] = None
        self.dolphin_status = CONNECTION_INITIAL_STATUS
        self.game_id = None
        self.awaiting_rom = False
        self.awaiting_server = True
        self.invalid_rom = False
        self.last_rcvd_index = -1
        self.has_send_death = False
        self.unlocked_stages = []
        self.unlocked_chrs = []
        self.unlocked_gears = [GEAR_DEFAULT]

        self.items_to_handle = []
        self.handled = []

        self.junk_delay = 0

        self.emeralds = []

        self.initialised = False
        self.stage_loading = False

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.auth = None
        await super().disconnect(allow_autoreconnect)

    def run_gui(self):
        from kvui import GameManager

        class SonicRidersManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago Sonic Riders"

        self.ui = SonicRidersManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    async def server_auth(self, username_requested: bool = True, password_requested: bool = False,
                          expectedUsername: str = None):
        if username_requested and not self.auth:
            await super(SonicRidersContext, self).get_username()
            if expectedUsername is not None and self.username != expectedUsername:
                self.auth = None
        if password_requested and not self.password:
            await super(SonicRidersContext, self).server_auth(password_requested)
        if not self.auth:
            if self.awaiting_rom:
                return
            self.awaiting_rom = True
            logger.info("Awaiting connection to Dolphin to get player information")
            return
        logger.info("Auth complete, connecting")
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.awaiting_server = False
        elif cmd == "ReceivedItems":
            if args["index"] >= self.last_rcvd_index:
                self.last_rcvd_index = args["index"]
                for item in args["items"]:
                    self.items_to_handle.append((item, self.last_rcvd_index))
                    self.last_rcvd_index += 1
            self.items_to_handle.sort(key=lambda v: v[1])


async def check_save_loaded(ctx):
    loaded = False

    game_state = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.GAME_STATE, 1)
    game_state = int.from_bytes(game_state, "big")

    if game_state != GAME_STATES.MAIN_MENU:
        loaded = True
        first_game_load = False
        loaded_index = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.SAVED_INDEX, 4)
        loaded_index = int.from_bytes(loaded_index, "big", signed=True)

        if loaded_index == 0:
            first_game_load = True

        if loaded and first_game_load:
            new_bytes = (-1).to_bytes(4, "big", signed=True)
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.SAVED_INDEX, new_bytes)

    return loaded


async def check_stage_status(ctx):
    last_unlocked_stages = ctx.unlocked_stages.copy()
    last_unlocked_chrs = ctx.unlocked_chrs.copy()
    last_unlocked_gears = ctx.unlocked_gears.copy()

    (final_location, stage_complete_locations, gear_complete_locations, chr_complete_locations,
     super_sonic_location) = Locations.get_all_location_info()

    info = Items.get_item_lookup_dict()

    si = [unlock for unlock in ctx.items_to_handle if unlock[0].item in info and info[unlock[0].item].type == "stage"]
    stages_to_unlock = [info[stage[0].item].stageId for stage in si]
    ctx.unlocked_stages.extend(stages_to_unlock)

    ci = [unlock for unlock in ctx.items_to_handle if unlock[0].item in info and info[unlock[0].item].type == "chr"]
    chrs_to_unlock = [info[char[0].item].chrId for char in ci]
    ctx.unlocked_chrs.extend(chrs_to_unlock)

    gi = [
        unlock for unlock in ctx.items_to_handle if unlock[0].item in info and
                                                    (info[unlock[0].item].type == "gear" or info[
                                                        unlock[0].item].type == "super sonic")
    ]
    gears_to_unlock = [info[gear[0].item].gearId for gear in gi]
    if CHR_EGGMAN in chrs_to_unlock:
        gears_to_unlock.append(GEAR_E_RIDER)
    if CHR_SHADOW in chrs_to_unlock:
        gears_to_unlock.append(GEAR_DARKNESS)
    ctx.unlocked_gears.extend(gears_to_unlock)

    remove = []
    for six in si:
        ctx.handled.append(six)
        remove.append(six)
    for cix in ci:
        ctx.handled.append(cix)
        remove.append(cix)
    for gix in gi:
        ctx.handled.append(gix)
        remove.append(gix)

    for r in remove:
        ctx.items_to_handle.remove(r)

    item_behaviour_changed = False
    if ctx.unlocked_stages != last_unlocked_stages or ctx.unlocked_chrs != last_unlocked_chrs or \
            ctx.unlocked_gears != last_unlocked_gears:
        item_behaviour_changed = True

    game_state = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.GAME_STATE, 1)
    game_state = int.from_bytes(game_state)

    if ctx.stage_loading and game_state != GAME_STATES.LOADING:
        ctx.stage_loading = False
        item_behaviour_changed = True  # Reset Characters

    new_stage_array = bytearray(16)
    old_stage_array = bytearray(dolphin_memory_engine.read_bytes(GAME_ADDRESSES.STAGE_ARRAY, 16))

    new_chr_array = bytearray(17)
    old_chr_array = bytearray(dolphin_memory_engine.read_bytes(GAME_ADDRESSES.CHR_ARRAY, 17))

    new_gear_board_array = bytearray(25)
    new_gear_bike_array = bytearray(10)
    new_gear_skates_array = bytearray(6)
    old_gear_board_array = bytearray(dolphin_memory_engine.read_bytes(GAME_ADDRESSES.GEAR_ARRAY_BOARD, 25))
    old_gear_bike_array = bytearray(dolphin_memory_engine.read_bytes(GAME_ADDRESSES.GEAR_ARRAY_BIKE, 10))
    old_gear_skates_array = bytearray(dolphin_memory_engine.read_bytes(GAME_ADDRESSES.GEAR_ARRAY_SKATES, 6))

    if item_behaviour_changed:

        for stage in STAGE_ID_TO_NAME.keys():
            if stage in ctx.unlocked_stages:
                new_stage_array[stage - 1] = 1
        if new_stage_array != old_stage_array:
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.STAGE_ARRAY, bytes(new_stage_array))

        for chr_id in CHR_ID_TO_NAME.keys():
            if chr_id in ctx.unlocked_chrs:
                new_chr_array[chr_id] = 1
        if new_chr_array != old_chr_array:
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.CHR_ARRAY, bytes(new_chr_array))

        for gear in GEAR_ID_TO_NAME.keys():
            if gear in ctx.unlocked_gears:
                if gear >= GEAR_DARKNESS:
                    new_gear_skates_array[gear - GEAR_DARKNESS] = 1
                elif gear >= GEAR_E_RIDER:
                    new_gear_bike_array[gear - GEAR_E_RIDER] = 1
                else:
                    new_gear_board_array[gear] = 1
        if new_gear_board_array != old_gear_board_array:
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.GEAR_ARRAY_BOARD, bytes(new_gear_board_array))
        if new_gear_bike_array != old_gear_bike_array:
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.GEAR_ARRAY_BIKE, bytes(new_gear_bike_array))
        if new_gear_skates_array != old_gear_skates_array:
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.GEAR_ARRAY_SKATES, bytes(new_gear_skates_array))

    found_emerald_items = [
        unlock for unlock in ctx.items_to_handle if unlock[0].item in info and info[unlock[0].item].type == "emerald"
    ]

    remove = []
    for ix in found_emerald_items:
        item_no = ix[0].item
        if item_no not in ctx.emeralds:
            ctx.emeralds.append(item_no)
        ctx.handled.append(ix)
        remove.append(ix)

    for r in remove:
        ctx.items_to_handle.remove(r)

    emeralds = Items.get_all_item_info()[1]
    emeralds_complete = True
    for emerald in emeralds:
        matches = [e for e in ctx.emeralds if e == emerald.itemId + BASE_ID]
        if len(matches) == 0:
            emeralds_complete = False
    if emeralds_complete:
        messages = [super_sonic_location[0].locationId + BASE_ID]
        message = [{"cmd": 'LocationChecks', "locations": messages}]
        await ctx.send_msgs(message)

    if game_state in [GAME_STATES.LOADING, GAME_STATES.STAGE_SELECT]:
        finish_time = bytearray(3)
        dolphin_memory_engine.write_bytes(GAME_ADDRESSES.PLAYER_FINISH_TIME, bytes(finish_time))
        ctx.stage_loading = True
        default = bytearray(17)
        for i in range(17):
            default[i] = 1
            if i > CHR_WAVE and i not in ctx.unlocked_chrs:
                default[i] = 0

        dolphin_memory_engine.write_bytes(GAME_ADDRESSES.CHR_ARRAY, bytes(default))

    current_stage = None

    if game_state in GAME_STATES.RACE:
        current_stage = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.CURRENT_STAGE, 4)
        current_stage = int.from_bytes(current_stage, "big")

        race_type = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.RACE_TYPE, 4)
        race_type = int.from_bytes(race_type, "big")
        if race_type != 700:
            return None

    return current_stage


async def handle_junk(ctx, current_stage):
    info = Items.get_item_lookup_dict()

    game_state = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.GAME_STATE, 1)
    game_state = int.from_bytes(game_state)

    if ctx.junk_delay > 0:
        if game_state not in GAME_STATES.RACE:
            ctx.junk_delay = 0
        else:
            ctx.junk_delay -= 1
            return

    current_lap = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.PLAYER_LAP, 1)
    current_lap = int.from_bytes(current_lap)

    if current_lap == 0:
        return  # Race has not started don't "waste" filler

    last_index = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.SAVED_INDEX, 4)
    last_index = int.from_bytes(last_index, signed=True)

    filler = [(unlock, info[unlock[0].item]) for unlock in ctx.items_to_handle if unlock[0].item in info and
              info[unlock[0].item].classification == ItemClass.filler and unlock[1] > last_index]

    latest_index: Optional[int] = None

    if len(filler) > 0:
        latest_index = max([u[0][1] for u in filler])

    filler_nothing = [f for f in filler if f[1].name == Junk.Nothing]
    filler_rings = [f for f in filler if f[1].type == "rings"]

    newly_handled = []
    newly_handled.extend([f[0] for f in filler_nothing])

    ring_limit = 100

    if len(filler_rings) > 0:
        current_rings = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.PLAYER_RINGS, 4)
        current_rings = int.from_bytes(current_rings)
        rings_changed = False

        for ring_junk in filler_rings:
            if current_rings >= ring_limit:
                break

            current_rings += ring_junk[1].value
            newly_handled.append(ring_junk[0])
            rings_changed = True

        if rings_changed:
            new_bytes = current_rings.to_bytes(4, byteorder='big')
            dolphin_memory_engine.write_bytes(GAME_ADDRESSES.PLAYER_RINGS, new_bytes)

    remove = []
    for r in newly_handled:
        ctx.handled.append(r)
        remove.append(r)

    for r in remove:
        ctx.items_to_handle.remove(r)

    if latest_index is not None:
        new_bytes = latest_index.to_bytes(4, signed=True)
        dolphin_memory_engine.write_bytes(GAME_ADDRESSES.SAVED_INDEX, new_bytes)


async def update_stage_behaviour(ctx, current_stage):
    (final_location, stage_complete_locations, gear_complete_locations, chr_complete_locations,
     super_sonic_location) = Locations.get_all_location_info()

    info = Items.get_item_lookup_dict()

    await handle_junk(ctx, current_stage)

    player_chr = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.PLAYER_CHR, 1)
    player_chr = int.from_bytes(player_chr)

    player_gear = dolphin_memory_engine.read_bytes(GAME_ADDRESSES.PLAYER_GEAR, 1)
    player_gear = int.from_bytes(player_gear)

    finish_time = bytearray(dolphin_memory_engine.read_bytes(GAME_ADDRESSES.PLAYER_FINISH_TIME, 3))
    finish_time = [t for t in finish_time]

    messages = []
    if finish_time[0] != 0 or finish_time[1] != 0 or finish_time[2] != 0:
        for stage_complete_location in stage_complete_locations:
            if stage_complete_location.stageId == current_stage:
                messages.append(stage_complete_location.locationId + BASE_ID)

        if player_chr == CHR_SUPER_SONIC:
            player_chr = CHR_SONIC
        for chr_complete_location in chr_complete_locations:
            if chr_complete_location.chrId == player_chr:
                messages.append(chr_complete_location.locationId + BASE_ID)

        for gear_complete_location in gear_complete_locations:
            if gear_complete_location.gearId == player_gear:
                if player_gear == GEAR_DEFAULT:
                    if gear_complete_location.chrId == player_chr:
                        messages.append(gear_complete_location.locationId + BASE_ID)
                else:
                    messages.append(gear_complete_location.locationId + BASE_ID)

        if current_stage == STAGE_BABYLON_GUARDIAN and player_gear == GEAR_CHAOS_EMERALD:
            await ctx.send_msgs([{
                "cmd": "StatusUpdate",
                "status": ClientStatus.CLIENT_GOAL,
            }])

    if len(messages) > 0:
        message = [{"cmd": 'LocationChecks', "locations": messages}]
        await ctx.send_msgs(message)


async def dolphin_sync_task(ctx: SonicRidersContext):
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    while not ctx.exit_event.is_set():
        death = False
        try:
            if ctx.slot is not None:
                pass
            else:
                # if not ctx.auth:
                #    # ctx.auth = read_string(SLOT_NAME_ADDR, 0x40)
                if ctx.awaiting_rom:
                    await ctx.server_auth()

            if dolphin_memory_engine.is_hooked() and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                if ctx.invalid_rom:
                    await ctx.disconnect()
                    await asyncio.sleep(5)

                elif ctx.awaiting_server:
                    await asyncio.sleep(1)
                    continue

                if True:
                    if not ctx.initialised:
                        ctx.initialised = True

                    if not await check_save_loaded(ctx):
                        await asyncio.sleep(0.1)
                        continue

                    stage = await check_stage_status(ctx)
                    if stage is not None:
                        await update_stage_behaviour(ctx, stage)

                await asyncio.sleep(0.1)
            else:
                if ctx.dolphin_status == CONNECTION_CONNECTED_STATUS and not ctx.invalid_rom:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                if ctx.invalid_rom:
                    logger.error("Invalid rom modification.")
                    break
                logger.info("Attempting to connect to Dolphin...")
                dolphin_memory_engine.hook()
                if dolphin_memory_engine.is_hooked():
                    # Hook and check the game?!
                    game_id_bytes = dolphin_memory_engine.read_bytes(0x80000000, 6)
                    if game_id_bytes != bytes(SONIC_RIDERS_ID, "utf-8"):
                        logger.info(CONNECTION_REFUSED_GAME_STATUS.format("", str(game_id_bytes)))
                        ctx.dolphin_status = CONNECTION_REFUSED_GAME_STATUS
                        dolphin_memory_engine.un_hook()
                        await asyncio.sleep(5)
                    else:
                        logger.info(CONNECTION_CONNECTED_STATUS)
                        ctx.dolphin_status = CONNECTION_CONNECTED_STATUS
                        ctx.game_id = game_id_bytes
                        # ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    await asyncio.sleep(5)
                    continue
        except Exception as e:
            logger.error(e)
            dolphin_memory_engine.un_hook()
            logger.info("Connection to Dolphin failed with exception, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = CONNECTION_LOST_STATUS
            # resetGameState(ctx)
            await ctx.disconnect(True)
            await asyncio.sleep(5)
            continue


def main(connect=None, password=None):
    Utils.init_logging("Sonic Riders Client")

    async def _main(connect, password):
        ctx = SonicRidersContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await asyncio.sleep(3)
            await ctx.dolphin_sync_task

    import colorama

    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)
