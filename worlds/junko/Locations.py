from typing import Dict

from BaseClasses import Location, Region
from ..AutoWorld import World

INTRO_REVOLVER = 1

INTRO_ID_TO_NAME = {
    INTRO_REVOLVER: "Revolver"
}
ALL_INTRO = list(INTRO_ID_TO_NAME.keys())

APT_BEDROOM_KEY = 2
APT_HALLWAY_BUTTON = 3
APT_HALLWAY_LION_BUTTON = 4

APT_ID_TO_NAME = {
    APT_BEDROOM_KEY: "Apt. Boarded Bedroom Silver Key",
    APT_HALLWAY_BUTTON: "Apt. Hallway Green Button",
    APT_HALLWAY_LION_BUTTON: "Apt. Hallway Lion Door Purple Button"
}
ALL_APT = list(APT_ID_TO_NAME.keys())

INSIDES_HIDDEN_BUTTON = 5
INSIDES_ACROSS_BRIDGE_BUTTON = 6
INSIDES_BEHIND_SPIKES_BUTTON = 7
INSIDES_BASEBALL = 8
INSIDES_BASEBALL_TOP_BUTTON = 9
INSIDES_BASEBALL_LEFT_BUTTON = 10
INSIDES_BASEBALL_RIGHT_BUTTON = 11
INSIDES_SHOP_BUTTONS = 12
INSIDES_MAP = 13
INSIDES_SHOP_KEY = 14
INSIDES_SHOP_BASEBALL = 15
INSIDES_SHOP_POWDER = 16
INSIDES_SHOP_DRINK = 17
INSIDES_CHEST = 18
INSIDES_BRAZIERS_BUTTON = 19
INSIDES_RAT_CLOAK = 20
INSIDES_RAT_BUTTON = 21
INSIDES_RAT_BASEBALL = 22
INSIDES_NEAR_CELLS_BUTTON = 23
INSIDES_CELLS_BUTTON = 24
INSIDES_CELLS_POWDER = 25
INSIDES_GAP_DRINK = 26
INSIDES_GATE_POWDER = 27
INSIDES_GATE_CRACK_BUTTON = 28

INSIDES_ID_TO_NAME = {
    INSIDES_HIDDEN_BUTTON: "Insides Hidden Blue Button",
    INSIDES_ACROSS_BRIDGE_BUTTON: "Insides Across Bridge Green Button",
    INSIDES_BEHIND_SPIKES_BUTTON: "Insides Behind Spikes Green Button",
    INSIDES_BASEBALL: "Insides Drop-Down Baseball",
    INSIDES_BASEBALL_TOP_BUTTON: "Insides Drop-Down Green Button (Top)",
    INSIDES_BASEBALL_LEFT_BUTTON: "Insides Drop-Down Green Button (Left)",
    INSIDES_BASEBALL_RIGHT_BUTTON: "Insides Drop-Down Green Button (Right)",
    INSIDES_SHOP_BUTTONS: "Insides Shop Purple Button",
    INSIDES_MAP: "Map",
    INSIDES_SHOP_KEY: "Insides Shop Silver Key",
    INSIDES_SHOP_BASEBALL: "Insides Shop Baseball",
    INSIDES_SHOP_POWDER: "Insides Shop Witch's Powder",
    INSIDES_SHOP_DRINK: "Insides Shop Loupa",
    INSIDES_CHEST: "Beth's Chest",
    INSIDES_BRAZIERS_BUTTON: "Insides Braziers Green Button",
    INSIDES_RAT_CLOAK: "Rat Cloak",
    INSIDES_RAT_BUTTON: "Insides Rat Tunnels Green Button",
    INSIDES_RAT_BASEBALL: "Insides Rat Tunnels Baseball",
    INSIDES_NEAR_CELLS_BUTTON: "Insides Near Cells Blue Button",
    INSIDES_CELLS_BUTTON: "Insides Cells Purple Button",
    INSIDES_CELLS_POWDER: "Insides Cells Witch's Powder",
    INSIDES_GAP_DRINK: "Insides Gap Loupa",
    INSIDES_GATE_POWDER: "Insides Behind Gate Witch's Powder",
    INSIDES_GATE_CRACK_BUTTON: "Insides Behind Gate Cracked Wall Blue Button",
}
ALL_INSIDES = list(INSIDES_ID_TO_NAME.keys())

RADIO_VENDING_BUTTON = 29
RADIO_HIDDEN_BUTTON = 30
RADIO_CRACK_DRINK = 31
RADIO_CRATES_BUTTON = 32
RADIO_SUNFLOWER = 33

RADIO_ID_TO_NAME = {
    RADIO_VENDING_BUTTON: "Radiation Vending Machine Green Button",
    RADIO_HIDDEN_BUTTON: "Radiation Hidden Green Button",
    RADIO_CRACK_DRINK: "Radiation Cracked Wall Loupa",
    RADIO_CRATES_BUTTON: "Radiation Crates Green Button",
    RADIO_SUNFLOWER: "Sunflower",
}
ALL_RADIO = list(RADIO_ID_TO_NAME.keys())

SECOND_SHED_BUTTON = 34
SECOND_WATER_BUTTON = 35
SECOND_PARLOR_HIDDEN_BUTTON = 36
SECOND_PARLOR_ALLEY_BUTTON = 37
SECOND_PIT_MAZE_BASEBALL = 38
SECOND_PIT_MAZE_LEFT_BUTTON = 39
SECOND_PIT_MAZE_RIGHT_BUTTON = 40
SECOND_PIT_MAZE_TOP_BUTTON = 41
SECOND_HOLES_ISOLATED_BUTTON = 42
SECOND_HOLES_BRIDGE_BUTTON = 43
SECOND_HOLES_RIGHT_BUTTON = 44
SECOND_PANPON_BOXES_BUTTON = 45
SECOND_PANPON_KEY = 46
SECOND_PANPON_HIDDEN_BUTTON = 47
SECOND_PANPON_FALSE_BUTTON = 48
SECOND_PANPON_MIRROR = 49
SECOND_HIDDEN_CRACK_BUTTON = 50
SECOND_ILLUSION_BUTTON = 51
SECOND_ILLUSION_KEY = 52
SECOND_ILLUSION_DRINK = 53
SECOND_MIRROR = 54
SECOND_RING = 55

SECOND_ID_TO_NAME = {
    SECOND_SHED_BUTTON: "2nd St. Spider's Shed Green Button",
    SECOND_WATER_BUTTON: "2nd St. Waterside Green Button",
    SECOND_PARLOR_HIDDEN_BUTTON: "Betting Parlor Hidden Crack Blue Button",
    SECOND_PARLOR_ALLEY_BUTTON: "2nd St. Betting Parlor Alley Green Button",
    SECOND_PIT_MAZE_BASEBALL: "Ohashi Building Baseball",
    SECOND_PIT_MAZE_LEFT_BUTTON: "Ohashi Building Left Green Button",
    SECOND_PIT_MAZE_RIGHT_BUTTON: "Ohashi Building Right Green Button",
    SECOND_PIT_MAZE_TOP_BUTTON: "Ohashi Building Purple Button",
    SECOND_HOLES_ISOLATED_BUTTON: "Hima Building Blue Button",
    SECOND_HOLES_BRIDGE_BUTTON: "Hima Building Bridge Green Button",
    SECOND_HOLES_RIGHT_BUTTON: "Hima Building Right Wall Green Button",
    SECOND_PANPON_BOXES_BUTTON: "Pan-Pon Boxes Green Button",
    SECOND_PANPON_KEY: "Pan-Pon (False) Silver Key",
    SECOND_PANPON_HIDDEN_BUTTON: "Pan-Pon (False) Hidden Purple Button",
    SECOND_PANPON_FALSE_BUTTON: "Pan-Pon (False) Green Button",
    SECOND_PANPON_MIRROR: "Mirror (Checkered Ensemble)",
    SECOND_HIDDEN_CRACK_BUTTON: "2nd St. Hidden Crack Purple Button",
    SECOND_ILLUSION_BUTTON: "Yagami Building Green Button",
    SECOND_ILLUSION_KEY: "Yagami Building Silver Key",
    SECOND_ILLUSION_DRINK: "Yagami Building Cracked Wall Loupa",
    SECOND_MIRROR: "Mirror (Casual Jeans)",
    SECOND_RING: "Ring Of Illusions",
}
ALL_SECOND = list(SECOND_ID_TO_NAME.keys())

ALLEY_PUMPKIN = 56
ALLEY_CRACKED_LEFT_BUTTON = 57
ALLEY_CRACKED_RIGHT_BUTTON = 58

ALLEY_ID_TO_NAME = {
    ALLEY_PUMPKIN: "Pumpkin",
    ALLEY_CRACKED_LEFT_BUTTON: "Alleyway Building Cracked Wall Green Button",
    ALLEY_CRACKED_RIGHT_BUTTON: "Alleyway Building Cracked Wall Blue Button",
}
ALL_ALLEY = list(ALLEY_ID_TO_NAME.keys())

FIELD_PATH_DIG_BUTTON = 59
FIELD_FENCE_DIG_BUTTON = 60
FIELD_GRASS_BUTTON = 61
FIELD_GRASS_DIG_BUTTON = 62
FIELD_HAT = 63
FIELD_POWDER = 72

FIELD_ID_TO_NAME = {
    FIELD_PATH_DIG_BUTTON: "Swirling Woods Path Dighole Green Button",
    FIELD_FENCE_DIG_BUTTON: "Swirling Woods Fence Dighole Green Button",
    FIELD_GRASS_BUTTON: "Swirling Woods Blue Button",
    FIELD_GRASS_DIG_BUTTON: "Swirling Woods Grass Dighole Green Button",
    FIELD_HAT: "Black Hat",
    FIELD_POWDER: "Insides Field Witch's Powder",
}
ALL_FIELD = list(FIELD_ID_TO_NAME.keys())

WOODS_BUTTON = 64
WOODS_FESTIVAL_DIG_BUTTON = 65
WOODS_MIRROR = 66
WOODS_FESTIVAL_BUTTON = 67
WOODS_BACKPACK = 68
WOODS_SHRINE_BUTTON = 69

WOODS_ID_TO_NAME = {
    WOODS_BUTTON: "Dark Woods Blue Button",
    WOODS_FESTIVAL_DIG_BUTTON: "Festival of Lights Dighole Blue Button",
    WOODS_MIRROR: "Mirror (Bright Yukata)",
    WOODS_FESTIVAL_BUTTON: "Festival of Lights Green Button",
    WOODS_BACKPACK: "Backpack",
    WOODS_SHRINE_BUTTON: "Festival Shrine Blue Button"
}
ALL_WOODS = list(WOODS_ID_TO_NAME.keys())

SANDS_DIG_BUTTON = 70
SANDS_ROCK_BUTTON = 71
SANDS_KEY = 73
SANDS_CAVE_BUTTON = 74
SANDS_NEAR_TAR_BUTTON = 75
SANDS_SALOON_DRINK = 76
SANDS_SALOON_BASEMENT_BUTTON = 77
SANDS_SALOON_ROOM_BUTTON = 78
SANDS_TAR_BARRELS_BUTTON = 79
SANDS_TAR_KEY = 80
SANDS_TAR_MIRROR = 81
SANDS_TAR_MIRROR_BUTTON = 82
SANDS_CAVE_FLG_BUTTON = 83
SANDS_CAVE_BLG_BUTTON = 84
SANDS_CAVE_BRG_BUTTON = 85
SANDS_CAVE_FRG_BUTTON = 86
SANDS_CAVE_LB_BUTTON = 87
SANDS_CAVE_MB_BUTTON = 88
SANDS_CAVE_RB_BUTTON = 89
SANDS_CAVE_P_BUTTON = 90
SANDS_HOT_FENCE_BUTTON = 91
SANDS_HOT_GREY_BUTTON = 92
SANDS_HOT_RUINS_BUTTON = 93
SANDS_HOT_BONE = 94

SANDS_ID_TO_NAME = {
    SANDS_DIG_BUTTON: "Burning Sands Dighole Blue Button",
    SANDS_ROCK_BUTTON: "Burning Sands Rock Green Button",
    SANDS_KEY: "Burning Sands Silver Key",
    SANDS_CAVE_BUTTON: "Burning Sands Near Cave Green Button",
    SANDS_NEAR_TAR_BUTTON: "Burning Sands Near The Pits Green Button",
    SANDS_SALOON_DRINK: "Spider Saloon Loupa",
    SANDS_SALOON_BASEMENT_BUTTON: "Spider Saloon Basement Cracked Wall Blue Button",
    SANDS_SALOON_ROOM_BUTTON: "Spider Saloon Locked Room Purple Button",
    SANDS_TAR_BARRELS_BUTTON: "The Pits Barrels Green Button",
    SANDS_TAR_KEY: "The Pits Silver Key",
    SANDS_TAR_MIRROR: "Mirror (Stretched Sweater)",
    SANDS_TAR_MIRROR_BUTTON: "The Pits Near Mirror Green Button",
    SANDS_CAVE_FLG_BUTTON: "Desert Treasure Cave Front Left Green Button",
    SANDS_CAVE_BLG_BUTTON: "Desert Treasure Cave Back Left Green Button",
    SANDS_CAVE_BRG_BUTTON: "Desert Treasure Cave Back Right Green Button",
    SANDS_CAVE_FRG_BUTTON: "Desert Treasure Cave Front Right Green Button",
    SANDS_CAVE_LB_BUTTON: "Desert Treasure Cave Left Blue Button",
    SANDS_CAVE_MB_BUTTON: "Desert Treasure Cave Middle Blue Button",
    SANDS_CAVE_RB_BUTTON: "Desert Treasure Cave Right Blue Button",
    SANDS_CAVE_P_BUTTON: "Desert Treasure Cave Purple Button",
    SANDS_HOT_FENCE_BUTTON: "Burning Sands Hot Fence Blue Button",
    SANDS_HOT_GREY_BUTTON: "Burning Sands Hot Grey Blue Button",
    SANDS_HOT_RUINS_BUTTON: "Burning Sands Hot Ruins Blue Button",
    SANDS_HOT_BONE: "Bone",
}
ALL_SANDS = list(SANDS_ID_TO_NAME.keys())

SNOW_STAIRS_BUTTON = 95
SNOW_BEHIND_BAR_KEY = 96
SNOW_SPRINGS_BUTTON = 97
SNOW_SPRINGS_KEY = 98
SNOW_CROWN = 99
SNOW_BAR_BUTTON = 100
SNOW_FREEZER_VOID_BUTTON = 101
SNOW_FREEZER_ICE = 102
SNOW_MINES_G_BUTTON = 103
SNOW_MINES_B_BUTTON = 104
SNOW_MINES_CABIN_BUTTON = 105
SNOW_CABIN_FISH = 106
SNOW_MINES_MIRROR = 107

SNOW_ID_TO_NAME = {
    SNOW_STAIRS_BUTTON: "Snow Drifts Near Stairs Blue Button",
    SNOW_BEHIND_BAR_KEY: "Snow Drifts Behind Bunny Bar Silver Key",
    SNOW_SPRINGS_BUTTON: "Hot Springs Purple Button",
    SNOW_SPRINGS_KEY: "Hot Springs Silver Key",
    SNOW_CROWN: "Dreamer's Crown",
    SNOW_BAR_BUTTON: "Bunny Bar Basement Purple Button",
    SNOW_FREEZER_VOID_BUTTON: "The Freezer Void Blue Button",
    SNOW_FREEZER_ICE: "Ice Cube",
    SNOW_MINES_G_BUTTON: "Minefield Green Button",
    SNOW_MINES_B_BUTTON: "Minefield Blue Button",
    SNOW_MINES_CABIN_BUTTON: "Minefield By Cabin Blue Button",
    SNOW_CABIN_FISH: "Fish",
    SNOW_MINES_MIRROR: "Mirror (Arcaust Uniform)",
}
ALL_SNOW = list(SNOW_ID_TO_NAME.keys())

FIRST_ALLEY_BUTTON = 108

FIRST_ALLEY_ID_TO_NAME = {
    FIRST_ALLEY_BUTTON: "1st St. Green Button"
}
ALL_FIRST_ALLEY = list(FIRST_ALLEY_ID_TO_NAME.keys())

FIRST_WELL_BUTTON = 109
FIRST_JUNKYARD_BUTTON = 110
FIRST_DIG_BUTTON = 111
FIRST_JUNKYARD_INSIDE_BUTTON = 112
FIRST_GARAGE_POWDER = 113
FIRST_GARAGE_MIRROR = 114
FIRST_HEART_BUTTON = 115
FIRST_HEART_EGG = 116

FIRST_ID_TO_NAME = {
    FIRST_WELL_BUTTON: "1st St. Well Blue Button",
    FIRST_JUNKYARD_BUTTON: "1st St. Outside Junkyard Green Button",
    FIRST_DIG_BUTTON: "1st St. Dighole Green Button",
    FIRST_JUNKYARD_INSIDE_BUTTON: "Junkyard Entrance Blue Button",
    FIRST_GARAGE_POWDER: "Lost Garage Witch's Powder",
    FIRST_GARAGE_MIRROR: "Mirror (Sailor Outfit)",
    FIRST_HEART_BUTTON: "Heart to Heart Club Green Button",
    FIRST_HEART_EGG: "Egg"
}
ALL_FIRST = list(FIRST_ID_TO_NAME.keys())

GUTTER_BUTTON = 117
GUTTER_SCYTHE = 118

GUTTER_ID_TO_NAME = {
    GUTTER_BUTTON: "The Gutter Purple Button",
    GUTTER_SCYTHE: "Scythe Blade"
}
ALL_GUTTER = list(GUTTER_ID_TO_NAME.keys())

RAVE_DIG_BUTTON = 119
RAVE_GRAVE_DRINK = 120
RAVE_KEY = 165

RAVE_ID_TO_NAME = {
    RAVE_DIG_BUTTON: "The Raveyard Dighole Purple Button",
    RAVE_GRAVE_DRINK: "The Raveyard Grave Loupa",
    RAVE_KEY: "The Raveyard Silver Key",
}
ALL_RAVE = list(RAVE_ID_TO_NAME.keys())

SHEOL_CRYPT_BUTTON = 121
SHEOL_LION_KEY = 122

SHEOL_ID_TO_NAME = {
    SHEOL_CRYPT_BUTTON: "The Crypt HIDDEN Orange Button",
    SHEOL_LION_KEY: "Lion Key"
}
ALL_SHEOL = list(SHEOL_ID_TO_NAME.keys())

THIRD_EGO_BUTTON = 123
THIRD_WATER_BUTTON = 124
THIRD_ABANDON_BASEBALL = 125
THIRD_ABANDON_BUTTON = 126
THIRD_SATURN_BUTTON = 127
THIRD_RUT_KEY = 128
THIRD_BEAR_BUTTON = 129
THIRD_BEAR_BELL = 130
THIRD_GALLERY_KEY = 131
THIRD_SNOW_QUILL = 132
THIRD_PERVERT_BUTTON = 133

THIRD_ID_TO_NAME = {
    THIRD_EGO_BUTTON: "3rd St. By Ego Green Button",
    THIRD_WATER_BUTTON: "3rd St. By Water Green Button",
    THIRD_ABANDON_BASEBALL: "Abandoned Place Baseball",
    THIRD_ABANDON_BUTTON: "Abandoned Place Blue Button",
    THIRD_SATURN_BUTTON: "Saturn Room Blue Button",
    THIRD_RUT_KEY: "The Rut Silver Key",
    THIRD_BEAR_BUTTON: "Junko's *NEW* Home Purple Button",
    THIRD_BEAR_BELL: "Bell",
    THIRD_GALLERY_KEY: "Art Gallery Silver Key",
    THIRD_SNOW_QUILL: "Quill",
    THIRD_PERVERT_BUTTON: "Pervert's Room Purple Button",
}
ALL_THIRD = list(THIRD_ID_TO_NAME.keys())

CANAL_ENTRANCE_KEY = 134
CANAL_PUMPKIN_BUTTON = 135
CANAL_DOWNSTAIRS_BUTTON = 136
CANAL_ELEVATOR_BASEBALL = 137
CANAL_CROWN_ENCHANT = 138

CANAL_ID_TO_NAME = {
    CANAL_ENTRANCE_KEY: "The Canals Entrance Silver Key",
    CANAL_PUMPKIN_BUTTON: "The Canals Pumpkin Green Button",
    CANAL_DOWNSTAIRS_BUTTON: "The Canals Downstairs Green Button",
    CANAL_ELEVATOR_BASEBALL: "The Canals Elevator Baseball",
    CANAL_CROWN_ENCHANT: "Dreamer's Crown Enchant",
}
ALL_CANAL = list(CANAL_ID_TO_NAME.keys())

FOURTH_VENDING_BUTTON = 139
FOURTH_ALLEY_BUTTON = 140
FOURTH_CLUB_HIDDEN_BUTTON = 141
FOURTH_DESERT_BUTTON = 142
FOURTH_DESERT_MIRROR = 143
FOURTH_DESERT_POWDER = 144
FOURTH_DESERT_RADSUIT = 145
FOURTH_HUNTER_ROOSTER = 146
FOURTH_HUNTER_BUTTON = 147
FOURTH_POKER_BUTTON = 148
FOURTH_HOSPITAL_HEART = 149

FOURTH_ID_TO_NAME = {
    FOURTH_VENDING_BUTTON: "4th St. Vending Machine Green Button",
    FOURTH_ALLEY_BUTTON: "4th St. Alley Green Button",
    FOURTH_CLUB_HIDDEN_BUTTON: "Gentleman's Club Hidden Crack Blue Button",
    FOURTH_DESERT_BUTTON: "False Desert Purple Button",
    FOURTH_DESERT_MIRROR: "Mirror (Magic Striped Shirt)",
    FOURTH_DESERT_POWDER: "False Desert Witch's Powder",
    FOURTH_DESERT_RADSUIT: "Radsuit",
    FOURTH_HUNTER_ROOSTER: "Rooster",
    FOURTH_HUNTER_BUTTON: "Hunter's House Green Button",
    FOURTH_POKER_BUTTON: "The Hangout Blue Button",
    FOURTH_HOSPITAL_HEART: "Heart"
}
ALL_FOURTH = list(FOURTH_ID_TO_NAME.keys())

HOSPITAL_GATE_BUTTON = 150
HOSPITAL_HALL_BUTTON = 151
HOSPITAL_FIG_BUTTON = 152
HOSPITAL_FIG = 153

HOSPITAL_ID_TO_NAME = {
    HOSPITAL_GATE_BUTTON: "Peeper's Hospital Gate Blue Button",
    HOSPITAL_HALL_BUTTON: "Peeper's Hospital Hallway Blue Button",
    HOSPITAL_FIG_BUTTON: "Peeper's Hospital Before Fig Leaf Blue Button",
    HOSPITAL_FIG: "Fig Leaf"
}
ALL_HOSPITAL = list(HOSPITAL_ID_TO_NAME.keys())

MEMORY_BUTTON = 154

MEMORY_ID_TO_NAME = {
    MEMORY_BUTTON: "Memory Lane Behind House Purple Button",
}
ALL_MEMORY = list(MEMORY_ID_TO_NAME.keys())

EGO_FIDDLE = 155

EGO_ID_TO_NAME = {
    EGO_FIDDLE: "Fiddle"
}
ALL_EGO = list(EGO_ID_TO_NAME.keys())

ROOM_PHONE = 156

ROOM_ID_TO_NAME = {
    ROOM_PHONE: "Phone?",
}
ALL_ROOM = list(ROOM_ID_TO_NAME.keys())

SCHOOL_SCYTHE = 157
# TODO Schoolsanity

SCHOOL_ID_TO_NAME = {
    SCHOOL_SCYTHE: "Scythe Handle"
}
ALL_SCHOOL = list(SCHOOL_ID_TO_NAME)

DEATH_ROCKS = 158

DEATH_ID_TO_NAME = {
    DEATH_ROCKS: "Strange Rocks"
}
ALL_DEATH = list(DEATH_ID_TO_NAME.keys())

FIFTH_DIG_BUTTON = 159
FIFTH_ALLEY_BUTTON = 160
FIFTH_APT_UNLOCK_BUTTON = 161
FIFTH_APT_REFILL_BUTTON = 162
FIFTH_HYPNO_BUTTON = 163
FIFTH_HYPNO_EARS = 164

FIFTH_ID_TO_NAME = {
    FIFTH_DIG_BUTTON: "5th St. Dighole Green Button",
    FIFTH_ALLEY_BUTTON: "5th St. Alley Green Button",
    FIFTH_APT_UNLOCK_BUTTON: "The Friendly Apt. Green Button",
    FIFTH_APT_REFILL_BUTTON: "The Friendly Apt. Blue Button",
    FIFTH_HYPNO_BUTTON: "The Hypnotist's Place Blue Button",
    FIFTH_HYPNO_EARS: "Bear Cub Ears"
}
ALL_FIFTH = list(FIFTH_ID_TO_NAME.keys())


class JunkoLocation(Location):
    game = "Junko"

    def __init__(self, player, location_name, location_id, region):
        super().__init__(player, location_name, location_id, region)


def get_location_dict():
    result = {}

    for introId in ALL_INTRO:
        result[INTRO_ID_TO_NAME[introId]] = introId

    for aptId in ALL_APT:
        result[APT_ID_TO_NAME[aptId]] = aptId

    for insidesID in ALL_INSIDES:
        result[INSIDES_ID_TO_NAME[insidesID]] = insidesID

    for radioId in ALL_RADIO:
        result[RADIO_ID_TO_NAME[radioId]] = radioId

    for secondId in ALL_SECOND:
        result[SECOND_ID_TO_NAME[secondId]] = secondId

    for alleyId in ALL_ALLEY:
        result[ALLEY_ID_TO_NAME[alleyId]] = alleyId

    for fieldId in ALL_FIELD:
        result[FIELD_ID_TO_NAME[fieldId]] = fieldId

    for woodsId in ALL_WOODS:
        result[WOODS_ID_TO_NAME[woodsId]] = woodsId

    for sandsId in ALL_SANDS:
        result[SANDS_ID_TO_NAME[sandsId]] = sandsId

    for snowId in ALL_SNOW:
        result[SNOW_ID_TO_NAME[snowId]] = snowId

    for firstAlleyId in ALL_FIRST_ALLEY:
        result[FIRST_ALLEY_ID_TO_NAME[firstAlleyId]] = firstAlleyId

    for firstId in ALL_FIRST:
        result[FIRST_ID_TO_NAME[firstId]] = firstId

    for gutterId in ALL_GUTTER:
        result[GUTTER_ID_TO_NAME[gutterId]] = gutterId

    for raveId in ALL_RAVE:
        result[RAVE_ID_TO_NAME[raveId]] = raveId

    for sheolId in ALL_SHEOL:
        result[SHEOL_ID_TO_NAME[sheolId]] = sheolId

    for thirdId in ALL_THIRD:
        result[THIRD_ID_TO_NAME[thirdId]] = thirdId

    for canalID in ALL_CANAL:
        result[CANAL_ID_TO_NAME[canalID]] = canalID

    for fourthId in ALL_FOURTH:
        result[FOURTH_ID_TO_NAME[fourthId]] = fourthId

    for hospitalId in ALL_HOSPITAL:
        result[HOSPITAL_ID_TO_NAME[hospitalId]] = hospitalId

    for memoryId in ALL_MEMORY:
        result[MEMORY_ID_TO_NAME[memoryId]] = memoryId

    for egoId in ALL_EGO:
        result[EGO_ID_TO_NAME[egoId]] = egoId

    for roomId in ALL_ROOM:
        result[ROOM_ID_TO_NAME[roomId]] = roomId

    for schoolId in ALL_SCHOOL:
        result[SCHOOL_ID_TO_NAME[schoolId]] = schoolId

    for deathID in ALL_DEATH:
        result[DEATH_ID_TO_NAME[deathID]] = deathID

    for fifthId in ALL_FIFTH:
        result[FIFTH_ID_TO_NAME[fifthId]] = fifthId

    return result


def create_locations(world: World, regions: Dict[str, Region]):
    intro_region = regions["Intro"]
    for introId in ALL_INTRO:
        loc = JunkoLocation(world.player, INTRO_ID_TO_NAME[introId], introId, intro_region)
        intro_region.locations.append(loc)

    apt_region = regions["Junko's Apartment"]
    for aptId in ALL_APT:
        loc = JunkoLocation(world.player, APT_ID_TO_NAME[aptId], aptId, apt_region)
        apt_region.locations.append(loc)

    insides_region = regions["The Insides"]
    for insideId in ALL_INSIDES:
        loc = JunkoLocation(world.player, INSIDES_ID_TO_NAME[insideId], insideId, insides_region)
        insides_region.locations.append(loc)

    radio_region = regions["Radiation Room"]
    for radioId in ALL_RADIO:
        loc = JunkoLocation(world.player, RADIO_ID_TO_NAME[radioId], radioId, radio_region)
        radio_region.locations.append(loc)

    second_region = regions["2nd Street"]
    for secondId in ALL_SECOND:
        loc = JunkoLocation(world.player, SECOND_ID_TO_NAME[secondId], secondId, second_region)
        second_region.locations.append(loc)

    alley_region = regions["The Alleyway"]
    for alleyId in ALL_ALLEY:
        loc = JunkoLocation(world.player, ALLEY_ID_TO_NAME[alleyId], alleyId, alley_region)
        alley_region.locations.append(loc)

    field_region = regions["Swirling Woods"]
    for fieldId in ALL_FIELD:
        loc = JunkoLocation(world.player, FIELD_ID_TO_NAME[fieldId], fieldId, field_region)
        field_region.locations.append(loc)

    woods_region = regions["Dark Woods"]
    for woodsId in ALL_WOODS:
        loc = JunkoLocation(world.player, WOODS_ID_TO_NAME[woodsId], woodsId, woods_region)
        woods_region.locations.append(loc)

    sands_region = regions["Burning Sands"]
    for sandsId in ALL_SANDS:
        loc = JunkoLocation(world.player, SANDS_ID_TO_NAME[sandsId], sandsId, sands_region)
        sands_region.locations.append(loc)

    snow_region = regions["Snow Drifts"]
    for snowId in ALL_SNOW:
        loc = JunkoLocation(world.player, SNOW_ID_TO_NAME[snowId], snowId, snow_region)
        snow_region.locations.append(loc)

    first_alley_region = regions["1st Alleyway"]
    for firstAlleyId in ALL_FIRST_ALLEY:
        loc = JunkoLocation(world.player, FIRST_ALLEY_ID_TO_NAME[firstAlleyId], firstAlleyId, first_alley_region)
        first_alley_region.locations.append(loc)

    first_region = regions["1st Street"]
    for firstId in ALL_FIRST:
        loc = JunkoLocation(world.player, FIRST_ID_TO_NAME[firstId], firstId, first_region)
        first_region.locations.append(loc)

    gutter_region = regions["The Gutter"]
    for gutterId in ALL_GUTTER:
        loc = JunkoLocation(world.player, GUTTER_ID_TO_NAME[gutterId], gutterId, gutter_region)
        gutter_region.locations.append(loc)

    rave_region = regions["The Raveyard"]
    for raveId in ALL_RAVE:
        loc = JunkoLocation(world.player, RAVE_ID_TO_NAME[raveId], raveId, rave_region)
        rave_region.locations.append(loc)

    sheol_region = regions["Sheol"]
    for sheolId in ALL_SHEOL:
        loc = JunkoLocation(world.player, SHEOL_ID_TO_NAME[sheolId], sheolId, sheol_region)
        sheol_region.locations.append(loc)

    third_region = regions["3rd Street"]
    for thirdId in ALL_THIRD:
        loc = JunkoLocation(world.player, THIRD_ID_TO_NAME[thirdId], thirdId, third_region)
        third_region.locations.append(loc)

    canal_region = regions["The Canals"]
    for canalId in ALL_CANAL:
        loc = JunkoLocation(world.player, CANAL_ID_TO_NAME[canalId], canalId, canal_region)
        canal_region.locations.append(loc)

    fourth_region = regions["4th Street"]
    for fourthId in ALL_FOURTH:
        loc = JunkoLocation(world.player, FOURTH_ID_TO_NAME[fourthId], fourthId, fourth_region)
        fourth_region.locations.append(loc)

    hospital_region = regions["Peeper's Hospital"]
    for hospitalId in ALL_HOSPITAL:
        loc = JunkoLocation(world.player, HOSPITAL_ID_TO_NAME[hospitalId], hospitalId, hospital_region)
        hospital_region.locations.append(loc)

    memory_region = regions["Memory Lane"]
    for memoryId in ALL_MEMORY:
        loc = JunkoLocation(world.player, MEMORY_ID_TO_NAME[memoryId], memoryId, memory_region)
        memory_region.locations.append(loc)

    ego_region = regions["Ego Street"]
    for egoId in ALL_EGO:
        loc = JunkoLocation(world.player, EGO_ID_TO_NAME[egoId], egoId, ego_region)
        ego_region.locations.append(loc)

    room_region = regions["The Purple Room"]
    for roomId in ALL_ROOM:
        loc = JunkoLocation(world.player, ROOM_ID_TO_NAME[roomId], roomId, room_region)
        room_region.locations.append(loc)

    school_region = regions["Purple School"]
    for schoolId in ALL_SCHOOL:
        loc = JunkoLocation(world.player, SCHOOL_ID_TO_NAME[schoolId], schoolId, school_region)
        school_region.locations.append(loc)

    death_region = regions["Death"]
    for deathId in ALL_DEATH:
        loc = JunkoLocation(world.player, DEATH_ID_TO_NAME[deathId], deathId, death_region)
        death_region.locations.append(loc)

    fifth_region = regions["5th Street"]
    for fifthId in ALL_FIFTH:
        loc = JunkoLocation(world.player, FIFTH_ID_TO_NAME[fifthId], fifthId, fifth_region)
        fifth_region.locations.append(loc)
