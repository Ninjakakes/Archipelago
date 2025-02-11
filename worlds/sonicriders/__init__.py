from typing import ClassVar, Dict

from BaseClasses import Tutorial, Item
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import components, Component, Type, launch_subprocess

from . import Regions, Locations, Rules
from .Items import SonicRidersItem
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
    """In Sonic Riders, Dr. Eggman challenges Sonic and his friends to a Worldwide Grand Prix, and the prize for 
    coming out on top is an ultra-rare Chaos Emerald! Gliding on air boards – which are performance-oriented for each 
    playable character – gamers will experience a heightened sense of sports-style racing tension as Sonic and his 
    pals perform tricks and stunts over treacherous wide-open terrain."""
    game = "Sonic Riders"
    web = SonicRidersWeb()

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
        return "Nothing"

    def set_rules(self) -> None:
        Rules.set_rules(self.multiworld, self, self.player)
