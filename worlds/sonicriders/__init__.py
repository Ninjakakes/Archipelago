from typing import ClassVar, Dict, Mapping, Any

from BaseClasses import Tutorial, Item
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import components, Component, Type, launch_subprocess

from . import Regions, Locations, Rules
from .Items import SonicRidersItem
from .Options import SonicRidersOptions
from .Stages import *
from .Gears import *
from .Characters import *


def run_client():
    from .SonicRidersClient import main
    print("Running SonicRidersClient")

    launch_subprocess(main, name="SonicRidersClient")


components.append(
    Component(
        "Sonic Riders Client",
        func=run_client,
        component_type=Type.CLIENT,
    )
)


class SonicRidersWeb(WebWorld):
    theme = "jungle"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Sonic Riders for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ninjakakes"]
    )


class SonicRidersWorld(World):
    """
    In Sonic Riders, Dr. Eggman challenges Sonic and his friends to a Worldwide Grand Prix, and the prize for
    coming out on top is an ultra-rare Chaos Emerald! Gliding on air boards – which are performance-oriented for each 
    playable character – gamers will experience a heightened sense of sports-style racing tension as Sonic and his 
    pals perform tricks and stunts over treacherous wide-open terrain.
    """
    game = "Sonic Riders"
    web = SonicRidersWeb()

    options_dataclass = SonicRidersOptions
    options: SonicRidersOptions

    required_client_version = (0, 5, 1)

    item_name_to_id: ClassVar[Dict[str, int]] = Items.get_item_dict()
    location_name_to_id: ClassVar[Dict[str, int]] = Locations.get_location_dict()

    item_name_groups = Items.get_item_groups()

    def create_regions(self) -> None:
        regions = Regions.create_regions(self)
        Locations.create_locations(self, regions)
        self.multiworld.regions.extend(regions.values())

        for first_stages in self.first_stages:
            stage_item = STAGE_ID_TO_NAME[first_stages]
            self.options.start_inventory.value[stage_item] = 1
            self.multiworld.push_precollected(self.create_item(stage_item))

        for first_chr in self.first_chrs:
            chr_item = CHR_ID_TO_NAME[first_chr]
            self.options.start_inventory.value[chr_item] = 1
            self.multiworld.push_precollected((self.create_item(chr_item)))

    def create_item(self, name: str) -> Item:
        info = Items.get_item_by_name(name)
        return SonicRidersItem(info, self.player)

    def create_items(self) -> None:
        Items.populate_item_pool(self, self.first_stages, self.first_chrs)

    def get_filler_item_name(self) -> str:
        final_items, emerald_items, stage_items, gear_items, chr_items, junk_items = Items.get_all_item_info()
        item_info = Items.choose_junk_items(self.random, junk_items, self.options, 1)[0]
        return item_info.name

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "ring_link": self.options.ring_link.value,
            "death_link": self.options.death_link.value,

            "stage_top_three": self.options.stage_top_three.value,
            "stage_first_place": self.options.stage_first_place.value,

            "chr_top_three": self.options.character_top_three.value,
            "chr_first_place": self.options.character_first_place.value,

            "gear_top_three": self.options.gear_top_three.value,
            "gear_first_place": self.options.gear_first_place.value,
        }
        return slot_data

    def set_rules(self) -> None:
        Rules.set_rules(self.multiworld, self, self.player)
