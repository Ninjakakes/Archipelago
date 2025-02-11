from typing import Dict, Optional, Callable

from BaseClasses import Region, Entrance
from .Characters import *
from .Stages import *


def create_regions(world) -> Dict[str, Region]:
    regions: Dict[str, Region] = {}
    stages = ALL_STAGES

    stage_regions = []
    region_to_stage_id = {}
    possible_first_regions = []

    for stage_id in stages:
        region_name = STAGE_ID_TO_NAME[stage_id]
        new_region = Region(region_name, world.player, world.multiworld)
        regions[region_name] = new_region
        stage_regions.append(new_region)

        if stage_id in BASE_STAGES:
            possible_first_regions.append(new_region)

        region_to_stage_id[new_region] = stage_id

    first_regions = world.random.sample(possible_first_regions, 1)
    world.first_stages = [region_to_stage_id[region] for region in first_regions]

    world.first_chrs = world.random.sample(ALL_CHRS, 1)

    regions["Menu"] = Region("Menu", world.player, world.multiworld)

    for region in stage_regions:
        stage_id = region_to_stage_id[region]

        connect_name = "menu-to-stage-" + str(stage_id)
        source_region = regions["Menu"]
        stage_item_name = STAGE_ID_TO_NAME[stage_id]

        if stage_id in ALT_STAGES:
            base_region_name = STAGE_ID_TO_NAME[stage_id - 8]
            source_region = regions[base_region_name]

        connect(world.player, connect_name, source_region, region,
                lambda state, si=stage_item_name: state.has(si, world.player))

    return regions


def connect(player: int, name: str, source_region: Region, target_region: Region, rule: Optional[Callable] = None):
    connection = Entrance(player, name, source_region)

    if rule is not None:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection
