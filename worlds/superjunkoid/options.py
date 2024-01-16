from typing import Union

from super_junkoid_randomizer.defaultLogic import Default
from super_junkoid_randomizer.game import Game

from worlds.superjunkoid.location import location_data


def make_sj_game(seed: Union[int, None])-> Game:
    seed = seed or 0
    sj_game = Game(Default,location_data,seed)
    return sj_game
