from dataclasses import dataclass
from typing import Optional, Dict

from BaseClasses import Location, Region
from .Characters import *
from .Constants import *
from .Gears import *
from .Stages import *


class SonicRidersLocation(Location):
    game: str = "Sonic Riders"

    def __init__(self, player, location_name, location_id, region):
        super().__init__(player, location_name, location_id, region)


LOCATION_TYPE_STAGE_COMPLETE = 0
LOCATION_TYPE_GEAR_COMPLETE = 1
LOCATION_TYPE_CHARACTER_COMPLETE = 2
LOCATION_TYPE_OTHER = 3


@dataclass
class LocationInfo:
    location_type: int
    locationId: int
    name: str
    stageId: Optional[int]
    gearId: Optional[int]
    chrId: Optional[int]


def get_location_dict():
    all_locations = get_all_location_info()

    result = {}
    for location_type in all_locations:
        for location in location_type:
            result[location.name] = location.locationId + BASE_ID

    return result


def get_all_location_info():
    id_offset = 0

    stage_complete_locations = []
    stage_top_three = []
    stage_first_place = []
    gear_complete_locations = []
    gear_top_three = []
    gear_first_place = []
    chr_complete_locations = []
    chr_top_three = []
    chr_first_place = []

    final_location = LocationInfo(LOCATION_TYPE_OTHER, id_offset, "Defeat Babylon Guardian", STAGE_BABYLON_GUARDIAN,
                                  None, None)
    id_offset += 1

    for stage_id in ALL_STAGES:
        location = LocationInfo(LOCATION_TYPE_STAGE_COMPLETE, id_offset, STAGE_ID_TO_NAME[stage_id] + ": Race Complete",
                                stage_id, None, None)
        id_offset += 1
        stage_complete_locations.append(location)

        location = LocationInfo(LOCATION_TYPE_STAGE_COMPLETE, id_offset, STAGE_ID_TO_NAME[stage_id] + ": Top 3",
                                stage_id, None, None)
        id_offset += 1
        stage_top_three.append(location)

        location = LocationInfo(LOCATION_TYPE_STAGE_COMPLETE, id_offset, STAGE_ID_TO_NAME[stage_id] + ": 1st Place",
                                stage_id, None, None)
        id_offset += 1
        stage_first_place.append(location)

    for gear_id in ALL_GEARS:
        if gear_id == GEAR_DEFAULT:
            for chr_id in CHR_ID_TO_DEFAULT_GEAR_NAME:
                gear_name = CHR_ID_TO_DEFAULT_GEAR_NAME[chr_id]
                location = LocationInfo(LOCATION_TYPE_GEAR_COMPLETE, id_offset, gear_name + ": Race Complete",
                                        None, gear_id, chr_id)
                id_offset += 1
                gear_complete_locations.append(location)

                location = LocationInfo(LOCATION_TYPE_GEAR_COMPLETE, id_offset, gear_name + ": Top 3",
                                        None, gear_id, chr_id)
                id_offset += 1
                gear_top_three.append(location)

                location = LocationInfo(LOCATION_TYPE_GEAR_COMPLETE, id_offset, gear_name + ": 1st Place",
                                        None, gear_id, chr_id)
                id_offset += 1
                gear_first_place.append(location)
        else:
            location = LocationInfo(LOCATION_TYPE_GEAR_COMPLETE, id_offset,
                                    GEAR_ID_TO_NAME[gear_id] + ": Race Complete",
                                    None, gear_id, None)
            id_offset += 1
            gear_complete_locations.append(location)

            location = LocationInfo(LOCATION_TYPE_GEAR_COMPLETE, id_offset,
                                    GEAR_ID_TO_NAME[gear_id] + ": Top 3",
                                    None, gear_id, None)
            id_offset += 1
            gear_top_three.append(location)

            location = LocationInfo(LOCATION_TYPE_GEAR_COMPLETE, id_offset,
                                    GEAR_ID_TO_NAME[gear_id] + ": 1st Place",
                                    None, gear_id, None)
            id_offset += 1
            gear_first_place.append(location)

    for chr_id in ALL_CHRS:
        location = LocationInfo(LOCATION_TYPE_CHARACTER_COMPLETE, id_offset, CHR_ID_TO_NAME[chr_id] + ": Race Complete",
                                None, None, chr_id)
        id_offset += 1
        chr_complete_locations.append(location)

        location = LocationInfo(LOCATION_TYPE_CHARACTER_COMPLETE, id_offset, CHR_ID_TO_NAME[chr_id] + ": Top 3",
                                None, None, chr_id)
        id_offset += 1
        chr_top_three.append(location)

        location = LocationInfo(LOCATION_TYPE_CHARACTER_COMPLETE, id_offset, CHR_ID_TO_NAME[chr_id] + ": 1st Place",
                                None, None, chr_id)
        id_offset += 1
        chr_first_place.append(location)

    super_sonic_location = LocationInfo(LOCATION_TYPE_OTHER, id_offset, "Super Sonic Unlock", None, None, None)
    id_offset += 1

    return ([final_location], stage_complete_locations, stage_top_three, stage_first_place,
            gear_complete_locations, gear_top_three, gear_first_place,
            chr_complete_locations, chr_top_three, chr_first_place,
            [super_sonic_location])


def create_locations(world, regions: Dict[str, Region]):
    (final_location, stage_complete_locations, stage_top_three, stage_first_place,
     gear_complete_locations, gear_top_three, gear_first_place,
     chr_complete_locations, chr_top_three, chr_first_place,
     super_sonic_location) = get_all_location_info()

    for loc in stage_complete_locations:
        region = regions[STAGE_ID_TO_NAME[loc.stageId]]
        location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, region)
        region.locations.append(location)

    if world.options.stage_top_three:
        for loc in stage_top_three:
            region = regions[STAGE_ID_TO_NAME[loc.stageId]]
            location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, region)
            region.locations.append(location)

    if world.options.stage_first_place:
        for loc in stage_first_place:
            region = regions[STAGE_ID_TO_NAME[loc.stageId]]
            location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, region)
            region.locations.append(location)

    menu_region = regions["Menu"]

    for loc in final_location:
        bab_guard_region = regions[STAGE_ID_TO_NAME[STAGE_BABYLON_GUARDIAN]]
        location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, bab_guard_region)
        bab_guard_region.locations.append(location)

    for loc in gear_complete_locations:
        location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
        menu_region.locations.append(location)

    if world.options.gear_top_three:
        for loc in gear_top_three:
            location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
            menu_region.locations.append(location)

    if world.options.gear_first_place:
        for loc in gear_first_place:
            location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
            menu_region.locations.append(location)

    for loc in chr_complete_locations:
        location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
        menu_region.locations.append(location)

    if world.options.character_top_three:
        for loc in chr_top_three:
            location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
            menu_region.locations.append(location)

    if world.options.character_first_place:
        for loc in chr_first_place:
            location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
            menu_region.locations.append(location)

    for loc in super_sonic_location:
        location = SonicRidersLocation(world.player, loc.name, loc.locationId + BASE_ID, menu_region)
        menu_region.locations.append(location)


def count_locations(world):
    count = 0
    (final_location, stage_complete_locations, stage_top_three, stage_first_place,
     gear_complete_locations, gear_top_three, gear_first_place,
     chr_complete_locations, chr_top_three, chr_first_place,
     super_sonic_location) = get_all_location_info()

    count += len(stage_complete_locations)
    if world.options.stage_top_three:
        count += len(stage_top_three)
    if world.options.stage_first_place:
        count += len(stage_first_place)
    count += len(gear_complete_locations)
    if world.options.gear_top_three:
        count += len(gear_top_three)
    if world.options.gear_first_place:
        count += len(gear_first_place)
    count += len(chr_complete_locations)
    if world.options.character_top_three:
        count += len(chr_top_three)
    if world.options.character_first_place:
        count += len(chr_first_place)

    return count
