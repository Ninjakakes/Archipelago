import functools
from typing import Optional

from super_junkoid_randomizer.defaultLogic import location_logic
from super_junkoid_randomizer.item import Items

from BaseClasses import ItemClassification, Region, CollectionState
from Options import PerGameCommonOptions
from worlds.AutoWorld import WebWorld, World

from .location import name_to_id as _loc_name_to_id, SuperJunkoidLocation
from .item import name_to_id as _item_name_to_id, SuperJunkoidItem, names_for_item_pool
from .logic import cs_to_loadout, can_win
from .options import make_sj_game

from super_junkoid_randomizer.game import Game as SjGame


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

    sj_game: Optional[SjGame] = None

    def create_item(self, name: str) -> SuperJunkoidItem:
        return SuperJunkoidItem(name, self.player)

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
        count_h = 0 # 12 Hearts are progression , the rest are not
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
