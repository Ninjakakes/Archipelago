from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, DeathLink, Toggle


class RingLink(Choice):
    """
    Whether your ring gain/loss is linked to other players.
    Off disables the feature.
    On enables the feature
    Hard enable sending and receiving more difficult ring losses
    """
    display_name = "Ring Link"
    option_off = 0
    option_on = 1
    option_hard = 2
    default = option_off


class StageTopThree(Toggle):
    """
    Enables checks for placing in the top 3 in each stage
    """
    display_name = "Enable Stage Top 3"


class StageFirstPlace(Toggle):
    """
    Enables checks for placing first in each stage
    """
    display_name = "Enable Stage 1st Place"


class ChrTopThree(Toggle):
    """
    Enables checks for placing in the top 3 with each character
    """
    display_name = "Enable Character Top 3"


class ChrFirstPlace(Toggle):
    """
    Enables checks for placing first with each character
    """
    display_name = "Enable Character 1st Place"


class GearTopThree(Toggle):
    """
    Enables checks for placing in the top 3 with each gear
    """
    display_name = "Enable Gear Top 3"


class GearFirstPlace(Toggle):
    """
    Enables checks for placing first with each gear
    """
    display_name = "Enable Gear 1st Place"


@dataclass
class SonicRidersOptions(PerGameCommonOptions):
    ring_link: RingLink
    death_link: DeathLink

    stage_top_three: StageTopThree
    stage_first_place: StageFirstPlace

    character_top_three: ChrTopThree
    character_first_place: ChrFirstPlace

    gear_top_three: GearTopThree
    gear_first_place: GearFirstPlace
