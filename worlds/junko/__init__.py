from typing import ClassVar, Dict

from BaseClasses import Tutorial, ItemClassification as ItemClass, Item, LocationProgressType
from .Locations import SHEOL_ID_TO_NAME, SHEOL_CRYPT_BUTTON

from ..AutoWorld import WebWorld, World

from .Options import JunkoOptions
from .Items import JunkoItem, ACTIVE_ID_TO_NAME, REVOLVER
from . import Items, Regions, Locations, Rules


class JunkoWeb(WebWorld):
    theme = "ice"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Junko for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ninjakakes"]
    )


class JunkoWorld(World):
    """
    Junko was once the master of her own world, but the subjects that once served her no longer fear her.

    A Yume Nikki-inspired game developed by P. Yoshi for Leeble Game Jam 3.
    """
    game = "Junko"
    web = JunkoWeb()

    options_dataclass = JunkoOptions
    options: JunkoOptions

    item_name_to_id: ClassVar[Dict[str, int]] = Items.get_item_dict()
    location_name_to_id: ClassVar[Dict[str, int]] = Locations.get_location_dict()

    def create_regions(self) -> None:
        regions = Regions.create_regions(self)
        Locations.create_locations(self, regions)
        self.multiworld.regions.extend(regions.values())

    def create_item(self, name: str) -> Item:

        item_id = self.item_name_to_id[name]
        item_class = ItemClass.filler
        return JunkoItem(name, item_class, item_id, self.player)

    def create_items(self) -> None:
        Items.populate_item_pool(self, self.options)

    def get_filler_item_name(self) -> str:
        return Items.CONSUME_ID_TO_NAME[Items.FIVE_BUTTONS]

    def set_rules(self) -> None:
        Rules.set_rules(self.multiworld, self, self.player)

        if self.options.early_revolver == "early_global":
            self.multiworld.early_items[self.player][ACTIVE_ID_TO_NAME[REVOLVER]] = 1
        elif self.options.early_revolver == "early_local":
            self.multiworld.local_early_items[self.player][ACTIVE_ID_TO_NAME[REVOLVER]] = 1

        if self.options.exclude_HIDDEN_orange_button:
            loc = self.multiworld.get_location(SHEOL_ID_TO_NAME[SHEOL_CRYPT_BUTTON], self.player)
            loc.progress_type = LocationProgressType.EXCLUDED
