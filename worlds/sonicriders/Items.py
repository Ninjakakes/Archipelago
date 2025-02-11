from dataclasses import dataclass
from typing import List, Optional, Dict

from BaseClasses import Item, ItemClassification as ItemClass
from worlds.AutoWorld import World
from . import Locations
from .Stages import *
from .Gears import *
from .Characters import *
from .Constants import *


@dataclass
class ItemInfo:
    itemId: int
    name: str
    classification: ItemClass
    stageId: Optional[int]
    gearId: Optional[int]
    chrId: Optional[int]
    type: str
    value: Optional[int]


class Progression:
    BabylonTreasure = "The Treasure Of Babylon"
    WhiteEmerald = "White Chaos Emerald"
    RedEmerald = "Red Chaos Emerald"
    CyanEmerald = "Cyan Chaos Emerald"
    PurpleEmerald = "Purple Chaos Emerald"
    GreenEmerald = "Green Chaos Emerald"
    YellowEmerald = "Yellow Chaos Emerald"
    BlueEmerald = "Blue Chaos Emerald"


class Junk:
    Nothing = "Nothing"


RING_AMOUNTS = {
    1: 5,
    5: 10,
    10: 20,
    20: 25,
    30: 20,
    100: 1
}


class SonicRidersItem(Item):
    game = "Sonic Riders"

    def __init__(self, item: ItemInfo, player):
        super().__init__(item.name, item.classification, item.itemId + BASE_ID, player)


def get_final_item(id_offset: int):
    info = ItemInfo(id_offset, Progression.BabylonTreasure, ItemClass.progression, None, None, None, "final", None)

    return info, id_offset + 1


def get_emerald_items(id_offset: int):
    emeralds: List[ItemInfo] = [
        ItemInfo(id_offset, Progression.WhiteEmerald, ItemClass.progression, None, None, None, "emerald", None),
        ItemInfo(id_offset + 1, Progression.RedEmerald, ItemClass.progression, None, None, None, "emerald", None),
        ItemInfo(id_offset + 2, Progression.CyanEmerald, ItemClass.progression, None, None, None, "emerald", None),
        ItemInfo(id_offset + 3, Progression.PurpleEmerald, ItemClass.progression, None, None, None, "emerald", None),
        ItemInfo(id_offset + 4, Progression.GreenEmerald, ItemClass.progression, None, None, None, "emerald", None),
        ItemInfo(id_offset + 5, Progression.YellowEmerald, ItemClass.progression, None, None, None, "emerald", None),
        ItemInfo(id_offset + 6, Progression.BlueEmerald, ItemClass.progression, None, None, None, "emerald", None),
    ]
    return emeralds, id_offset + 7


def get_stage_items(id_offset: int):
    stage_items = []
    count = id_offset
    for stage_id in ALL_STAGES:
        item = ItemInfo(count, STAGE_ID_TO_NAME[stage_id], ItemClass.progression, stage_id, None, None, "stage", None)

        count += 1
        stage_items.append(item)

    return stage_items, count


def get_gear_items(id_offset: int):
    gear_items = []
    count = id_offset
    for gear_id in ALL_GEARS:
        item = ItemInfo(count, GEAR_ID_TO_NAME[gear_id], ItemClass.progression, None, gear_id, None, "gear", None)

        if gear_id == GEAR_CHAOS_EMERALD:
            item.type = "super sonic"

        count += 1
        gear_items.append(item)

    return gear_items, count


def get_chr_items(id_offset: int):
    chr_items = []
    count = id_offset
    for chr_id in ALL_CHRS:
        item = ItemInfo(count, CHR_ID_TO_NAME[chr_id], ItemClass.progression, None, None, chr_id, "chr", None)

        count += 1
        chr_items.append(item)

    return chr_items, count


def get_item_dict():
    all_items = get_all_item_info()

    result = {}
    for item_type in all_items:
        for item in item_type:
            result[item.name] = item.itemId + BASE_ID

    return result


def get_item_lookup_dict():
    all_items = get_all_item_info()

    result = {}
    for item_type in all_items:
        for item in item_type:
            result[item.itemId + BASE_ID] = item

    return result


def get_item_by_name(name):
    d = get_item_lookup_dict()
    name_map = {v.name: v for k, v in d.items()}
    return name_map[name]


def get_junk_item_info(id_offset: int):
    junk_items = []

    nothing = ItemInfo(id_offset, Junk.Nothing, ItemClass.filler, None, None, None, "nothing", None)
    junk_items.append(nothing)

    ring_items, id_offset = get_ring_items(id_offset + 1)
    junk_items.extend(ring_items)

    return junk_items, id_offset


def get_ring_items(id_offset):
    infos = []

    for amount in RING_AMOUNTS.keys():
        infos.append(ItemInfo(id_offset, str(amount) + " Ring" + ("" if amount == 1 else "s"), ItemClass.filler,
                              None, None, None, "rings", amount))
        id_offset += 1

    return infos, id_offset


def get_all_item_info():
    id_offset = 0
    final_item, id_offset = get_final_item(id_offset)
    emerald_items, id_offset = get_emerald_items(id_offset)
    stage_items, id_offset = get_stage_items(id_offset)
    gear_items, id_offset = get_gear_items(id_offset)
    chr_items, id_offset = get_chr_items(id_offset)
    junk_items, id_offset = get_junk_item_info(id_offset)

    return [final_item], emerald_items, stage_items, gear_items, chr_items, junk_items


def choose_junk_items(random, junk, options, junk_count):
    junk_distribution = {}

    junk_items = []
    total = 0

    # if ring filler:
    for r, c in RING_AMOUNTS.items():
        r_item = [j for j in junk if j.type == "rings" and j.value == r][0]
        junk_distribution[total] = c
        junk_items.append(r_item)
        total += 1

    randomised_indices = random.choices(list(junk_distribution.keys()), k=junk_count,
                                        weights=list(junk_distribution.values()))
    return [junk_items[k] for k in randomised_indices]


def populate_item_pool(world: World, first_stages, first_chrs):
    final_items, emerald_items, stage_items, gear_items, chr_items, junk_items = get_all_item_info()

    default_gears = [
        GEAR_DEFAULT,
        GEAR_CHAOS_EMERALD,
        GEAR_E_RIDER,
        GEAR_DARKNESS
    ]

    use_stage_items = [s for s in stage_items if s.stageId not in first_stages]
    use_gear_items = [g for g in gear_items if g.gearId not in default_gears]
    use_chr_items = [c for c in chr_items if c.chrId not in first_chrs]

    mw_em_items = [SonicRidersItem(e, world.player) for e in emerald_items]
    mw_stage_items = [SonicRidersItem(s, world.player) for s in use_stage_items]
    mw_gear_items = [SonicRidersItem(g, world.player) for g in use_gear_items]
    mw_chr_items = [SonicRidersItem(c, world.player) for c in use_chr_items]

    item_count = (len(mw_em_items) + len(mw_stage_items) + len(mw_gear_items) + len(mw_chr_items))
    location_count = Locations.count_locations(world)
    junk_count = location_count - item_count

    mw_filler_items = [SonicRidersItem(i, world.player)
                       for i in choose_junk_items(world.random, junk_items, world.options, junk_count)]

    world.multiworld.itempool += mw_em_items
    world.multiworld.itempool += mw_stage_items
    world.multiworld.itempool += mw_gear_items
    world.multiworld.itempool += mw_chr_items
    world.multiworld.itempool += mw_filler_items


def get_item_groups():
    final_items, emerald_items, stage_items, gear_items, chr_items, junk_items = get_all_item_info()

    item_groups: Dict[str, list] = {
        "Chaos Emeralds": [e.name for e in emerald_items],
        "Stages": [e.name for e in stage_items],
        "Characters": [e.name for e in chr_items],
        "Gears": [e.name for e in gear_items]
    }

    return item_groups
