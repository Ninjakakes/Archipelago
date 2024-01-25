import functools
import os
from threading import Event
from typing import Optional, Union, Dict, Any

from BaseClasses import ItemClassification, Region, CollectionState, MultiWorld
from Options import PerGameCommonOptions
from worlds.AutoWorld import WebWorld, World

from .client import SuperJunkoidSNIClient
from .location import name_to_id as _loc_name_to_id, SuperJunkoidLocation
from .item import name_to_id as _item_name_to_id, SuperJunkoidItem, names_for_item_pool
from .logic import cs_to_loadout, can_win
from .options import make_sj_game

from super_junkoid_randomizer.game import Game as SjGame
from super_junkoid_randomizer.defaultLogic import location_logic
from super_junkoid_randomizer.item import Items

from .patch_utils import ItemRomData, GenData, make_gen_data
from .rom import SuperJunkoidDeltaPatch

_ = SuperJunkoidSNIClient  # load the module to register the handler


class SuperJunkoidWebWorld(WebWorld):
    theme = "ice"


class SuperJunkoidWorld(World):
    """
    Trapped in a twisted dream where she is revered as a goddess, Junko must face the horrifying serpent that worships
    her.
    """
    game = "Super Junkoid"
    data_version = 0
    web = SuperJunkoidWebWorld()

    options_dataclass = PerGameCommonOptions
    options: PerGameCommonOptions

    location_name_to_id = _loc_name_to_id
    item_name_to_id = _item_name_to_id

    rom_name: Union[bytes, bytearray]
    rom_name_available_event: Event

    sj_game: Optional[SjGame] = None

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.rom_name = b""
        self.rom_name_available_event = Event()

    def create_item(self, name: str) -> SuperJunkoidItem:
        return SuperJunkoidItem(name, self.player)

    def generate_early(self) -> None:
        early_items = ["Feather", "Wallkicks", "Magic Broom"]
        early_item = self.multiworld.random.choice(early_items)
        self.multiworld.local_early_items[self.player][early_item] = 1

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)

        sj_game = make_sj_game(self.multiworld.seed)
        self.sj_game = sj_game

        for loc_name in _loc_name_to_id:
            loc = SuperJunkoidLocation(self.player, loc_name, menu)
            menu.locations.append(loc)

            def access_rule_wrapped(local_loc_name: str,
                                    local_sj_game: SjGame,
                                    p: int,
                                    collection_state: CollectionState) -> bool:
                loadout = cs_to_loadout(local_sj_game, collection_state, p)
                return location_logic[local_loc_name](loadout)

            access_rule = functools.partial(access_rule_wrapped,
                                            loc_name, self.sj_game, self.player)
            loc.access_rule = access_rule

            # completion condition
            def completion_wrapped(local_sj_game: SjGame,
                                   p: int,
                                   collection_state: CollectionState) -> bool:
                loadout = cs_to_loadout(local_sj_game, collection_state, p)
                return can_win in loadout

            completion = functools.partial(completion_wrapped, sj_game, self.player)
            self.multiworld.completion_condition[self.player] = completion

    def create_items(self) -> None:
        count_h = 0  # 12 Hearts are progression , the rest are not
        count_bb = 0  # 5 Baseballs are progression, the rest are not
        count_sps = 0  # 1 Sparksuit is progression, the rest are not
        for name in names_for_item_pool():
            this_item = self.create_item(name)
            if name == Items.Heart[0]:
                if count_h <= 12:
                    this_item.classification = ItemClassification.progression
                count_h += 1
            elif name == Items.Baseball[0]:
                if count_bb <= 5:
                    this_item.classification = ItemClassification.progression
                count_bb += 1
            elif name == Items.Sparksuit[0]:
                if count_sps == 0:
                    this_item.classification = ItemClassification.progression
                count_sps += 1
            self.multiworld.itempool.append(this_item)

    def generate_output(self, output_directory: str) -> None:
        assert self.sj_game, "can't call generate_output without create_regions"

        item_rom_data = ItemRomData(self.player, self.multiworld.player_name)
        for loc in self.multiworld.get_locations():
            item_rom_data.register(loc)

        # set rom name
        from Utils import __version__
        rom_name = bytearray(
            f'SJ{__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}',
            'utf8'
        )[:21]
        rom_name.extend(b" " * (21 - len(rom_name)))
        assert len(rom_name) == 21, f"{rom_name=}"
        self.rom_name = rom_name
        self.rom_name_available_event.set()

        gen_data = GenData(item_rom_data.get_jsonable_data(), self.sj_game, self.player, self.rom_name)

        out_file_base = self.multiworld.get_out_file_name_base(self.player)

        patch_file_name = os.path.join(output_directory, f"{out_file_base}{SuperJunkoidDeltaPatch.patch_file_ending}")
        patch = SuperJunkoidDeltaPatch(patch_file_name,
                                       player=self.player,
                                       player_name=self.multiworld.player_name[self.player],
                                       gen_data=make_gen_data(gen_data))

        patch.write()

    def modify_multidata(self, multidata: Dict[str, Any]) -> None:
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = self.rom_name
        assert len(rom_name) == 21, f"{rom_name=}"
        new_name = base64.b64encode(rom_name).decode()
        multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]
