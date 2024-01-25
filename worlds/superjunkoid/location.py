from typing import Optional

from BaseClasses import Location, Region
from .config import base_id

from super_junkoid_randomizer.location import Location as SjLocation, pullCSV

location_data = pullCSV()

id_to_name = {
    loc["index"] + base_id: loc_name
    for loc_name, loc in location_data.items()
}

name_to_id = {
    n: id_
    for id_, n in id_to_name.items()
}


class SuperJunkoidLocation(Location):
    game = "Super Junkoid"
    sj_loc: SjLocation

    def __init__(self,
                 player: int,
                 name: str,
                 parent: Optional[Region] = None) -> None:
        loc_id = name_to_id[name]
        super().__init__(player, name, loc_id, parent)
        self.sj_loc = location_data[name]
