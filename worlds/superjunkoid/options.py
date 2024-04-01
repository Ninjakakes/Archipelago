from dataclasses import dataclass
from typing import Union

from super_junkoid_randomizer.defaultLogic import Default
from super_junkoid_randomizer.game import Game

from Options import Choice, PerGameCommonOptions
from worlds.superjunkoid.location import location_data


class SuperJunkoidFirstItem(Choice):
    """
    Which movement item if any will apper at Hidden Pipe Heart

    None - no guaranteed first item expect to be BK'd until you receive one of the 3 movement items
    """
    display_name = "First Item"
    option_any = 0
    option_feather = 1
    option_wallkicks = 2
    option_magic_broom = 3
    option_none = 4
    default = 0

@dataclass
class SuperJunkoidOptions(PerGameCommonOptions):
    first_item: SuperJunkoidFirstItem


def make_sj_game(seed: Union[int, None]) -> Game:
    seed = seed or 0
    sj_game = Game(Default, location_data, seed)
    return sj_game
