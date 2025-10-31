from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, StartInventoryPool, Toggle


class EarlyRevolver(Choice):
    """
    Force Your Revolver into an early sphere in your world or across all worlds.
    """
    display_name = "Early Revolver"
    option_off = 0
    option_early_global = 1
    option_early_local = 2
    default = option_off


class ShuffleStrangeRocks(Toggle):
    """
    Shuffle the Strange Rocks into the multiworld or have them be given by death for collecting the scythe pieces
    """
    display_name = "Shuffle Strange Rocks"


@dataclass
class JunkoOptions(PerGameCommonOptions):
    early_revolver: EarlyRevolver

    shuffle_strange_rocks: ShuffleStrangeRocks

    start_inventory_from_pool: StartInventoryPool
