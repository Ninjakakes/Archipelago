from BaseClasses import MultiWorld
from worlds.AutoWorld import World
from worlds.generic.Rules import add_rule

from .Characters import *
from .Gears import *
from .Stages import *

CHR_TO_GEARS = {
    CHR_SONIC: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_BLUE_STAR_II, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP,
        GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_HOVERCRAFT, GEAR_CHAOS_EMERALD,
        GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK,
        GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_S, GEAR_HANG_ON, GEAR_SUPER_HANG_ON,
        GEAR_DARKNESS, GEAR_ADVANTAGE_S, GEAR_CANNONBALL
    ],
    CHR_TAILS: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER,
        GEAR_LEGEND, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY,
        GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_F,
        GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_F, GEAR_CANNONBALL
    ],
    CHR_KNUCKLES: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER,
        GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE,
        GEAR_OMNIPOTENCE, GEAR_COVER_P, GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_P,
        GEAR_CANNONBALL
    ],
    CHR_AMY: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER,
        GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER,
        GEAR_OMNIPOTENCE, GEAR_COVER_S, GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_ADVANTAGE_S,
        GEAR_CANNONBALL
    ],
    CHR_JET: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER,
        GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER,
        GEAR_OMNIPOTENCE, GEAR_COVER_S, GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_ADVANTAGE_S,
        GEAR_CANNONBALL
    ],
    CHR_STORM: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER,
        GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE,
        GEAR_OMNIPOTENCE, GEAR_COVER_P, GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_P,
        GEAR_CANNONBALL
    ],
    CHR_WAVE: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER,
        GEAR_LEGEND, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY,
        GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_F,
        GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_F, GEAR_CANNONBALL
    ],
    CHR_EGGMAN: [
        GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_OMNIPOTENCE, GEAR_COVER_P, GEAR_HANG_ON, GEAR_SUPER_HANG_ON
    ],
    CHR_CREAM: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER,
        GEAR_LEGEND, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY,
        GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_F,
        GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_F, GEAR_CANNONBALL
    ],
    CHR_ROUGE: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER,
        GEAR_LEGEND, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY,
        GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_F,
        GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_F, GEAR_CANNONBALL
    ],
    CHR_SHADOW: [
        GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR, GEAR_SPEED_BALANCER,
        GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER, GEAR_LEGEND,
        GEAR_MAGIC_CARPET, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY,
        GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_S,
        GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_ADVANTAGE_S, GEAR_CANNONBALL
    ],
    CHR_NIGHTS: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD, GEAR_SLIDE_BOOSTER,
        GEAR_LEGEND, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY,
        GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE, GEAR_DESTROYER, GEAR_OMNIPOTENCE, GEAR_COVER_F,
        GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_F, GEAR_CANNONBALL
    ],
    CHR_AIAI: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER,
        GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_E_RIDER, GEAR_AIR_TANK, GEAR_HEAVY_BIKE,
        GEAR_OMNIPOTENCE, GEAR_COVER_P, GEAR_HANG_ON, GEAR_SUPER_HANG_ON, GEAR_DARKNESS, GEAR_GRINDER, GEAR_ADVANTAGE_P,
        GEAR_CANNONBALL
    ],
    CHR_ULALA: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER,
        GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER, GEAR_DARKNESS, GEAR_ADVANTAGE_S, GEAR_CANNONBALL
    ],
    CHR_E10G: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_AIR_BROOM, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER,
        GEAR_POWER, GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER
    ],
    CHR_E10R: [
        GEAR_DEFAULT, GEAR_HIGH_BOOSTER, GEAR_AUTO_SLIDER, GEAR_POWERFUL, GEAR_FASTEST, GEAR_TURBO_STAR,
        GEAR_SPEED_BALANCER, GEAR_ACCESS, GEAR_BEGINNER, GEAR_ACCELERATOR, GEAR_TRAP, GEAR_LIGHT_BOARD,
        GEAR_SLIDE_BOOSTER, GEAR_LEGEND, GEAR_MAGIC_CARPET, GEAR_HOVERCRAFT, GEAR_FASTER, GEAR_GAMBLER, GEAR_POWER,
        GEAR_OPA_OPA, GEAR_CRAZY, GEAR_BERSERKER
    ]
}

GEAR_TO_CHR = {
    GEAR_DEFAULT: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_NIGHTS,
        CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_HIGH_BOOSTER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_AUTO_SLIDER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_POWERFUL: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_FASTEST: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_TURBO_STAR: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_SPEED_BALANCER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_BLUE_STAR_II: [
        CHR_SONIC
    ],
    GEAR_ACCESS: [
        CHR_SONIC, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_SHADOW, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_BEGINNER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_ACCELERATOR: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_TRAP: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_LIGHT_BOARD: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_SLIDE_BOOSTER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_LEGEND: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_MAGIC_CARPET: [
        CHR_SONIC, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_SHADOW, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_AIR_BROOM: [
        CHR_TAILS, CHR_KNUCKLES, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_NIGHTS, CHR_AIAI, CHR_E10G
    ],
    GEAR_HOVERCRAFT: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_CHAOS_EMERALD: [
        CHR_SONIC
    ],
    GEAR_FASTER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_GAMBLER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_POWER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_OPA_OPA: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_CRAZY: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_BERSERKER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA, CHR_E10G, CHR_E10R
    ],
    GEAR_E_RIDER: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_EGGMAN, CHR_CREAM, CHR_ROUGE,
        CHR_SHADOW, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_AIR_TANK: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_EGGMAN, CHR_CREAM, CHR_ROUGE,
        CHR_SHADOW, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_HEAVY_BIKE: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_EGGMAN, CHR_CREAM, CHR_ROUGE,
        CHR_SHADOW, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_DESTROYER: [
        CHR_SONIC, CHR_TAILS, CHR_AMY, CHR_JET, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW, CHR_NIGHTS
    ],
    GEAR_OMNIPOTENCE: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_EGGMAN, CHR_CREAM, CHR_ROUGE,
        CHR_SHADOW, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_COVER_S: [
        CHR_SONIC, CHR_AMY, CHR_JET, CHR_SHADOW
    ],
    GEAR_COVER_F: [
        CHR_TAILS, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_NIGHTS
    ],
    GEAR_COVER_P: [
        CHR_KNUCKLES, CHR_STORM, CHR_EGGMAN, CHR_AIAI
    ],
    GEAR_HANG_ON: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_EGGMAN, CHR_CREAM, CHR_ROUGE,
        CHR_SHADOW, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_SUPER_HANG_ON: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_EGGMAN, CHR_CREAM, CHR_ROUGE,
        CHR_SHADOW, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_DARKNESS: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA
    ],
    GEAR_GRINDER: [
        CHR_TAILS, CHR_KNUCKLES, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_NIGHTS, CHR_AIAI
    ],
    GEAR_ADVANTAGE_S: [
        CHR_SONIC, CHR_AMY, CHR_JET, CHR_SHADOW, CHR_ULALA
    ],
    GEAR_ADVANTAGE_F: [
        CHR_TAILS, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_NIGHTS
    ],
    GEAR_ADVANTAGE_P: [
        CHR_KNUCKLES, CHR_STORM, CHR_AIAI
    ],
    GEAR_CANNONBALL: [
        CHR_SONIC, CHR_TAILS, CHR_KNUCKLES, CHR_AMY, CHR_JET, CHR_STORM, CHR_WAVE, CHR_CREAM, CHR_ROUGE, CHR_SHADOW,
        CHR_NIGHTS, CHR_AIAI, CHR_ULALA
    ]
}


def set_rules(multiworld: MultiWorld, world, player: int):
    from . import Locations, Items
    from .Items import SonicRidersItem
    (final_location, stage_complete_locations, stage_top_three, stage_first_place,
     gear_complete_locations, gear_top_three, gear_first_place,
     chr_complete_locations, chr_top_three, chr_first_place,
     super_sonic_location) = Locations.get_all_location_info()
    final_items, emerald_items, stage_items, gear_items, chr_items, junk_items = Items.get_all_item_info()

    for chr_id in ALL_CHRS:
        chr_locs = [l for l in chr_complete_locations if l.chrId == chr_id]
        for loc in chr_locs:
            mw_chr_loc = multiworld.get_location(loc.name, player)
            add_rule(mw_chr_loc, lambda state, c=CHR_ID_TO_NAME[chr_id]: state.has(c, player))

        if world.options.character_top_three:
            chr_locs = [l for l in chr_top_three if l.chrId == chr_id]
            for loc in chr_locs:
                mw_chr_loc = multiworld.get_location(loc.name, player)
                add_rule(mw_chr_loc, lambda state, c=CHR_ID_TO_NAME[chr_id]: state.has(c, player))

        if world.options.character_first_place:
            chr_locs = [l for l in chr_first_place if l.chrId == chr_id]
            for loc in chr_locs:
                mw_chr_loc = multiworld.get_location(loc.name, player)
                add_rule(mw_chr_loc, lambda state, c=CHR_ID_TO_NAME[chr_id]: state.has(c, player))

    for stage_id in BASE_STAGES:
        stage_locs = [l for l in stage_complete_locations if l.stageId == stage_id]
        for loc in stage_locs:
            mw_stage_loc = multiworld.get_location(loc.name, player)
            add_rule(mw_stage_loc, lambda state, s=STAGE_ID_TO_NAME[stage_id]: state.has(s, player))

        if world.options.stage_top_three:
            stage_locs = [l for l in stage_top_three if l.stageId == stage_id]
            for loc in stage_locs:
                mw_stage_loc = multiworld.get_location(loc.name, player)
                add_rule(mw_stage_loc, lambda state, s=STAGE_ID_TO_NAME[stage_id]: state.has(s, player))

        if world.options.stage_first_place:
            stage_locs = [l for l in stage_first_place if l.stageId == stage_id]
            for loc in stage_locs:
                mw_stage_loc = multiworld.get_location(loc.name, player)
                add_rule(mw_stage_loc, lambda state, s=STAGE_ID_TO_NAME[stage_id]: state.has(s, player))

    for gear_id in ALL_GEARS:
        gear_locs = [l for l in gear_complete_locations if l.gearId == gear_id]
        for loc in gear_locs:
            mw_gear_loc = multiworld.get_location(loc.name, player)
            if gear_id == GEAR_E_RIDER:
                rule = lambda state, c=CHR_ID_TO_NAME[CHR_EGGMAN]: state.has(c, player)
            elif gear_id == GEAR_DARKNESS:
                rule = lambda state, c=CHR_ID_TO_NAME[CHR_SHADOW]: state.has(c, player)
            elif loc.chrId is not None:  # Default Gear
                rule = lambda state, c=CHR_ID_TO_NAME[loc.chrId]: state.has(c, player)
            else:
                valid_chrs = tuple([CHR_ID_TO_NAME[c] for c in GEAR_TO_CHR[gear_id]])
                rule = lambda state, g=GEAR_ID_TO_NAME[gear_id], c=valid_chrs: \
                    state.has(g, player) and state.has_any(c, player)
            add_rule(mw_gear_loc, rule)

        if world.options.gear_top_three:
            gear_locs = [l for l in gear_top_three if l.gearId == gear_id]
            for loc in gear_locs:
                mw_gear_loc = multiworld.get_location(loc.name, player)
                if gear_id == GEAR_E_RIDER:
                    rule = lambda state, c=CHR_ID_TO_NAME[CHR_EGGMAN]: state.has(c, player)
                elif gear_id == GEAR_DARKNESS:
                    rule = lambda state, c=CHR_ID_TO_NAME[CHR_SHADOW]: state.has(c, player)
                elif loc.chrId is not None:  # Default Gear
                    rule = lambda state, c=CHR_ID_TO_NAME[loc.chrId]: state.has(c, player)
                else:
                    valid_chrs = tuple([CHR_ID_TO_NAME[c] for c in GEAR_TO_CHR[gear_id]])
                    rule = lambda state, g=GEAR_ID_TO_NAME[gear_id], c=valid_chrs: \
                        state.has(g, player) and state.has_any(c, player)
                add_rule(mw_gear_loc, rule)

        if world.options.gear_first_place:
            gear_locs = [l for l in gear_first_place if l.gearId == gear_id]
            for loc in gear_locs:
                mw_gear_loc = multiworld.get_location(loc.name, player)
                if gear_id == GEAR_E_RIDER:
                    rule = lambda state, c=CHR_ID_TO_NAME[CHR_EGGMAN]: state.has(c, player)
                elif gear_id == GEAR_DARKNESS:
                    rule = lambda state, c=CHR_ID_TO_NAME[CHR_SHADOW]: state.has(c, player)
                elif loc.chrId is not None:  # Default Gear
                    rule = lambda state, c=CHR_ID_TO_NAME[loc.chrId]: state.has(c, player)
                else:
                    valid_chrs = tuple([CHR_ID_TO_NAME[c] for c in GEAR_TO_CHR[gear_id]])
                    rule = lambda state, g=GEAR_ID_TO_NAME[gear_id], c=valid_chrs: \
                        state.has(g, player) and state.has_any(c, player)
                add_rule(mw_gear_loc, rule)

    super_item = [g for g in gear_items if g.gearId == GEAR_CHAOS_EMERALD][0]
    mw_super_item = SonicRidersItem(super_item, player)
    mw_super_location = multiworld.get_location(super_sonic_location[0].name, player)
    mw_super_location.place_locked_item(mw_super_item)

    super_rule = lambda state: True
    for emerald in emerald_items:
        new_emerald = lambda state, en=emerald.name: state.has(en, player)
        super_rule = lambda state, sr=super_rule, ne=new_emerald: sr(state) and ne(state)
    add_rule(mw_super_location, super_rule)

    mw_final_item = SonicRidersItem(final_items[0], player)
    mw_final_location = multiworld.get_location(final_location[0].name, player)
    mw_final_location.place_locked_item(mw_final_item)

    add_rule(mw_final_location,
             lambda state:
             state.has(super_item.name, player) and
             state.has(CHR_ID_TO_NAME[CHR_SONIC], player) and
             state.has(STAGE_ID_TO_NAME[STAGE_BABYLON_GUARDIAN], player))

    multiworld.completion_condition[player] = lambda state: state.has(Items.Progression.BabylonTreasure, player)
