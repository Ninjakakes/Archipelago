from typing import Iterator, Tuple

from super_junkoid_randomizer.defaultLogic import killJunkraid, killJunkgon, junkoon, junkly
from super_junkoid_randomizer.game import Game
from super_junkoid_randomizer.loadout import Loadout
from super_junkoid_randomizer.logic_shortcut import LogicShortcut

from BaseClasses import CollectionState

from .item import name_to_id as item_name_to_id, id_to_sj_item


can_win = LogicShortcut(lambda loadout: (
        (killJunkraid in loadout) and (killJunkgon in loadout) and (junkoon in loadout) and (junkly in loadout)
))

def item_counts(cs: CollectionState, p: int) -> Iterator[Tuple[str, int]]:
    """
    the items that player p has collected

    ((item_name, count), (item_name, count), ...)
    """
    return ((item_name, cs.count(item_name, p)) for item_name in item_name_to_id)


def cs_to_loadout(sj_game: Game, collection_state: CollectionState, player: int) -> Loadout:
    """ convert Archipelago CollectionState to super_junkoid_randomizer loadout state """
    loadout = Loadout(sj_game)
    for item_name, count in item_counts(collection_state, player):
        loadout.contents[id_to_sj_item[item_name_to_id[item_name]]] += count
    return loadout
