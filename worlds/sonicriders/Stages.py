STAGE_METAL_CITY = 1
STAGE_SPLASH_CANYON = 2
STAGE_EGG_FACTORY = 3
STAGE_GREEN_CAVE = 4
STAGE_SAND_RUINS = 5
STAGE_BABYLON_GARDEN = 6
STAGE_DIGITAL_DIMENSION = 7
STAGE_SEGA_CARNIVAL = 8
STAGE_NIGHT_CHASE = 9
STAGE_RED_CANYON = 10
STAGE_ICE_FACTORY = 11
STAGE_WHITE_CAVE = 12
STAGE_DARK_DESERT = 13
STAGE_SKY_ROAD = 14
STAGE_BABYLON_GUARDIAN = 15
STAGE_SEGA_ILLUSION = 16

STAGE_ID_TO_NAME = {
    STAGE_METAL_CITY: "Metal City",
    STAGE_SPLASH_CANYON: "Splash Canyon",
    STAGE_EGG_FACTORY: "Egg Factory",
    STAGE_GREEN_CAVE: "Green Cave",
    STAGE_SAND_RUINS: "Sand Ruins",
    STAGE_BABYLON_GARDEN: "Babylon Garden",
    STAGE_DIGITAL_DIMENSION: "Digital Dimension",
    STAGE_SEGA_CARNIVAL: "SEGA CARNIVAL",
    STAGE_NIGHT_CHASE: "Night Chase",
    STAGE_RED_CANYON: "Red Canyon",
    STAGE_ICE_FACTORY: "Ice Factory",
    STAGE_WHITE_CAVE: "White Cave",
    STAGE_DARK_DESERT: "Dark Desert",
    STAGE_SKY_ROAD: "Sky Road",
    STAGE_BABYLON_GUARDIAN: "Babylon Guardian",
    STAGE_SEGA_ILLUSION: "SEGA ILLUSION"
}
ALL_STAGES = list(STAGE_ID_TO_NAME.keys())
BASE_STAGES = [x for x in ALL_STAGES if x <= STAGE_SEGA_CARNIVAL]
ALT_STAGES = [x for x in ALL_STAGES if x > STAGE_SEGA_CARNIVAL]
