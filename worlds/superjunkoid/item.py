from collections import defaultdict
from typing import Dict, Iterator

from BaseClasses import Item, ItemClassification as IC

from .config import base_id

from super_junkoid_randomizer.item import Item as SjItem, Items
from super_junkoid_randomizer.fillAssumed import FillAssumed

classifications: Dict[str, IC] = defaultdict(lambda: IC.progression)
classifications.update({
    Items.LuckyFrog[0]: IC.filler,
    Items.DeathGem[0]: IC.useful,
    Items.BigLeagueGlove[0]: IC.useful,
    Items.WaveBangle[0]: IC.filler,
    Items.MagicSoap[0]: IC.useful,
    Items.DreamersCrown[0]: IC.useful,
    Items.Heart[0]: IC.filler,  # 12 progression set by create_items
    Items.Baseball[0]: IC.filler,  # 5 progression set by create_items
    Items.Sparksuit[0]: IC.filler  # 1 progression set by create_items
})


class SuperJunkoidItem(Item):
    game = "Super Junkoid"
    __slots__ = ("sj_item",)
    sj_item: SjItem

    def __init__(self, name: str, player: int) -> None:
        classification = classifications[name]
        code = name_to_id[name]
        super().__init__(name, classification, code, player)
        self.sj_item = id_to_sj_item[code]


local_id_to_sj_item: Dict[int, SjItem] = {
    0x00: Items.Heart,
    0x01: Items.MagicBolt,
    0x02: Items.Baseball,
    0x03: Items.Sparksuit,
    0x04: Items.RatBurst,
    0x05: Items.DeathGem,
    0x06: Items.IceGem,
    0x07: Items.Feather,
    0x08: Items.RatDasher,
    0x09: Items.BloodGem,
    0x0a: Items.WaveBangle,
    0x0b: Items.PurpleLocket,
    0x0c: Items.SanguineFin,
    0x0d: Items.MagicSoap,
    0x0e: Items.StormsGem,
    0x0f: Items.DreamersCrown,
    0x10: Items.MagicBroom,
    0x11: Items.Wallkicks,
    0x12: Items.RatCloak,
    0x13: Items.LuckyFrog,
    0x14: Items.BigLeagueGlove
}

id_to_sj_item = {
    id_ + base_id: item
    for id_, item in local_id_to_sj_item.items()
}

name_to_id = {
    item[0]: id_
    for id_, item in id_to_sj_item.items()
}


def names_for_item_pool() -> Iterator[str]:
    sj_fill = FillAssumed()
    for sj_item in sj_fill.prog_items:
        yield sj_item[0]
    for sj_item in sj_fill.extra_items:
        yield sj_item[0]
