from typing import Optional, Callable

from BaseClasses import Entrance
from .Rules import *


def create_regions(world):
    regions: Dict[str, Region] = \
        {
            "Menu": Region("Menu", world.player, world.multiworld),
            "Intro": Region("Intro", world.player, world.multiworld),
            "Junko's Apartment": Region("Junko's Apartment", world.player, world.multiworld),
            "The Insides": Region("The Insides", world.player, world.multiworld),
            "Radiation Room": Region("Radiation Room", world.player, world.multiworld),
            "2nd Street": Region("2nd Street", world.player, world.multiworld),
            "The Alleyway": Region("The Alleyway", world.player, world.multiworld),
            "Swirling Woods": Region("Swirling Woods", world.player, world.multiworld),
            "Dark Woods": Region("Dark Woods", world.player, world.multiworld),
            "Burning Sands": Region("Burning Sands", world.player, world.multiworld),
            "Snow Drifts": Region("Snow Drifts", world.player, world.multiworld),
            "1st Alleyway": Region("1st Alleyway", world.player, world.multiworld),
            "1st Street": Region("1st Street", world.player, world.multiworld),
            "The Gutter": Region("The Gutter", world.player, world.multiworld),
            "The Raveyard": Region("The Raveyard", world.player, world.multiworld),
            "Sheol": Region("Sheol", world.player, world.multiworld),
            "3rd Street": Region("3rd Street", world.player, world.multiworld),
            "The Canals": Region("The Canals", world.player, world.multiworld),
            "4th Street": Region("4th Street", world.player, world.multiworld),
            "Peeper's Hospital": Region("Peeper's Hospital", world.player, world.multiworld),
            "Memory Lane": Region("Memory Lane", world.player, world.multiworld),
            "Ego Street": Region("Ego Street", world.player, world.multiworld),
            "The Purple Room": Region("The Purple Room", world.player, world.multiworld),
            "Purple School": Region("Purple School", world.player, world.multiworld),
            "Death": Region("Death", world.player, world.multiworld),
            "5th Street": Region("5th Street", world.player, world.multiworld),
        }

    connect(world.player, "Menu-to-Intro", regions["Menu"], regions["Intro"])

    connect(world.player, "Intro-to-Apt.", regions["Intro"], regions["Junko's Apartment"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[REVOLVER], world.player))

    connect(world.player, "Apt.-to-Insides", regions["Junko's Apartment"], regions["The Insides"])

    connect(world.player, "Insides-to-Radiation", regions["The Insides"], regions["Radiation Room"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[RADSUIT], world.player))

    connect(world.player, "Apt.-to-2nd", regions["Junko's Apartment"], regions["2nd Street"])

    connect(world.player, "2nd-to-Alley", regions["2nd Street"], regions["The Alleyway"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[BASEBALL], world.player) or can_fly(state, world.player))

    connect(world.player, "2nd-to-S.Woods", regions["2nd Street"], regions["Swirling Woods"])

    connect(world.player, "S.Woods-to-D.Woods", regions["Swirling Woods"], regions["Dark Woods"],
            lambda state:
            state.has(ACTIVE_ID_TO_NAME[HAT], world.player) and state.has(ACTIVE_ID_TO_NAME[SUNFLOWER], world.player))

    connect(world.player, "2nd-to-Sands", regions["2nd Street"], regions["Burning Sands"])

    connect(world.player, "Sands-to-Snow", regions["Burning Sands"], regions["Snow Drifts"])

    connect(world.player, "Alley-to-1stAlley", regions["The Alleyway"], regions["1st Alleyway"])
    connect(world.player, "1stAlley-to-Alley", regions["1st Alleyway"], regions["The Alleyway"])

    connect(world.player, "Insides-to-1stAlley", regions["The Insides"], regions["1st Alleyway"])

    connect(world.player, "2nd-to-1st", regions["2nd Street"], regions["1st Street"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[RING], world.player))

    connect(world.player, "1stAlley-to-1st", regions["1st Alleyway"], regions["1st Street"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[RING], world.player))
    connect(world.player, "1st-to-1stAlley", regions["1st Street"], regions["1st Alleyway"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[RING], world.player))

    connect(world.player, "1st-to-Gutter", regions["1st Street"], regions["The Gutter"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[FIDDLE], world.player) and
                          state.has(PASSIVE_ID_TO_NAME[LION_KEY], world.player) and
                          state.has(ACTIVE_ID_TO_NAME[SUNFLOWER], world.player))

    connect(world.player, "1st-to-Raveyard", regions["1st Street"], regions["The Raveyard"])

    connect(world.player, "Raveyard-to-Sheol", regions["The Raveyard"], regions["Sheol"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[EGG], world.player))

    connect(world.player, "2nd-to-3rd", regions["2nd Street"], regions["3rd Street"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[RING], world.player))

    connect(world.player, "3rd-to-Canals", regions["3rd Street"], regions["The Canals"],
            lambda state: can_fly(state, world.player) or state.has(ACTIVE_ID_TO_NAME[BASEBALL], world.player))

    connect(world.player, "3rd-to-4th", regions["3rd Street"], regions["4th Street"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[HAT], world.player))
    connect(world.player, "4th-to-3rd", regions["4th Street"], regions["3rd Street"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[HAT], world.player))

    connect(world.player, "S.Woods-to-4th", regions["Swirling Woods"], regions["4th Street"],
            lambda state:
            state.has(ACTIVE_ID_TO_NAME[HAT], world.player) and state.has(PASSIVE_ID_TO_NAME[RING], world.player))

    connect(world.player, "Gutter-to-4th", regions["The Gutter"], regions["4th Street"])

    connect(world.player, "Apt-to-4th", regions["Junko's Apartment"], regions["4th Street"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[ROOSTER], world.player))

    connect(world.player, "4th-to-Hospital", regions["4th Street"], regions["Peeper's Hospital"],
            lambda state:
            state.has(ACTIVE_ID_TO_NAME[BACKPACK], world.player) and
            state.has(PASSIVE_ID_TO_NAME[LION_KEY], world.player))

    connect(world.player, "4th-to-Memory", regions["4th Street"], regions["Memory Lane"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[LION_KEY], world.player))

    connect(world.player, "Memory-to-Sheol", regions["Memory Lane"], regions["Sheol"],
            lambda state: state.has(PASSIVE_ID_TO_NAME[LION_KEY], world.player))

    connect(world.player, "3rd-to-Ego", regions["3rd Street"], regions["Ego Street"],
            lambda state: can_fly(state, world.player))

    connect(world.player, "2nd-to-P.Room", regions["2nd Street"], regions["The Purple Room"],
            lambda state:
            (can_unlock(state, world.player) and can_buy(state, world.player, 500)) or
            (state.has(ACTIVE_ID_TO_NAME[PHONE], world.player) and state.has(ACTIVE_ID_TO_NAME[DRINK], world.player)))

    connect(world.player, "Apt-to-School", regions["Junko's Apartment"], regions["Purple School"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[FIG], world.player))

    connect(world.player, "Sheol-to-Death", regions["Sheol"], regions["Death"],
            lambda state:
            state.has(SCYTHE_ID_TO_NAME[SCYTHE_HANDLE], world.player) and
            state.has(SCYTHE_ID_TO_NAME[SCYTHE_BLADE], world.player))

    connect(world.player, "4th-to-5th", regions["4th Street"], regions["5th Street"])
    connect(world.player, "5th-to-4th", regions["5th Street"], regions["4th Street"])

    connect(world.player, "1st-to-5th", regions["1st Street"], regions["5th Street"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[HAT], world.player))
    connect(world.player, "5th-to-1st", regions["5th Street"], regions["1st Street"],
            lambda state: state.has(ACTIVE_ID_TO_NAME[HAT], world.player))

    return regions


def connect(player: int, name: str, source_region: Region, target_region: Region, rule: Optional[Callable] = None):
    connection = Entrance(player, name, source_region)

    if rule is not None:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection
