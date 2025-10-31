from BaseClasses import Item, ItemClassification as ItemClass
from ..AutoWorld import World
from . import JunkoOptions
from .Locations import DEATH_ID_TO_NAME, DEATH_ROCKS

REVOLVER = 1
BASEBALL = 2
POWDER = 3
DRINK = 4
PUMPKIN = 5
HAT = 6
FISH = 7
SUNFLOWER = 8
PHONE = 9
BEAR_CUB_EARS = 10
CROWN = 11
HEART = 12
FIG = 13
ICE = 14
RADSUIT = 15
BONE = 16
RAT = 17
BACKPACK = 18
BELL = 19
EGG = 20
FIDDLE = 21

ACTIVE_ID_TO_NAME = {
    REVOLVER: "Revolver",
    BASEBALL: "Baseball",
    POWDER: "Witch's Powder",
    DRINK: "Loupa",
    PUMPKIN: "Pumpkin",
    HAT: "Black Hat",
    FISH: "Fish",
    SUNFLOWER: "Sunflower",
    PHONE: "Phone?",
    BEAR_CUB_EARS: "Bear Cub Ears",
    CROWN: "Progressive Dreamer's Crown",
    HEART: "Heart",
    FIG: "Fig Leaf",
    ICE: "Ice Cube",
    RADSUIT: "Radsuit",
    BONE: "Bone",
    RAT: "Rat Cloak",
    BACKPACK: "Backpack",
    BELL: "Bell",
    EGG: "Egg",
    FIDDLE: "Fiddle"
}
ALL_ACTIVE = list(ACTIVE_ID_TO_NAME.keys())

QUILL = 22
CHEST = 23
ROCKS = 24
ROOSTER = 25
RING = 26
LION_KEY = 27

PASSIVE_ID_TO_NAME = {
    QUILL: "Ink & Quill",
    CHEST: "Beth's Chest",
    ROCKS: "Strange Rocks",
    ROOSTER: "Rooster",
    RING: "Ring Of Illusions",
    LION_KEY: "Lion Key"
}
ALL_PASSIVE = list(PASSIVE_ID_TO_NAME.keys())

SCYTHE_HANDLE = 28
SCYTHE_BLADE = 29

SCYTHE_ID_TO_NAME = {
    SCYTHE_HANDLE: "Scythe Handle",
    SCYTHE_BLADE: "Scythe Blade"
}
ALL_SCYTHE = list(SCYTHE_ID_TO_NAME.keys())

FIVE_BUTTONS = 30
TEN_BUTTONS = 31
TWENTY_FIVE_BUTTONS = 32
HUNDRED_BUTTONS = 33
KEY = 34

CONSUME_ID_TO_NAME = {
    FIVE_BUTTONS: "5 Buttons",
    TEN_BUTTONS: "10 Buttons",
    TWENTY_FIVE_BUTTONS: "25 Buttons",
    HUNDRED_BUTTONS: "100 Buttons",
    KEY: "Silver Key"
}
ALL_CONSUME = list(CONSUME_ID_TO_NAME.keys())

MAP = 35

JEANS = 36
YUKATA = 37
STRIPES = 38
SAILOR = 39
SWEATER = 40
ARCAUST = 41
CHECKERS = 42
HUNDO = 43


MIRROR_ID_TO_NAME = {
    JEANS: "Mirror (Casual Jeans)",
    YUKATA: "Mirror (Bright Yukata)",
    STRIPES: "Mirror (Magic Striped Shirt)",
    SAILOR: "Mirror (Sailor Outfit)",
    SWEATER: "Mirror (Stretched Sweater)",
    ARCAUST: "Mirror (Arcaust Uniform)",
    CHECKERS: "Mirror (Checkered Ensemble)",
    HUNDO: "Mirror (Ms. 100%)"
}
ALL_MIRROR = list(MIRROR_ID_TO_NAME.keys())


class JunkoItem(Item):
    game = "Junko"

    def __init__(self, name: str, classification: ItemClass, id: int, player):
        super().__init__(name, classification, id, player)


def get_item_dict():
    result = {}

    for activeId in ALL_ACTIVE:
        result[ACTIVE_ID_TO_NAME[activeId]] = activeId

    for passiveId in ALL_PASSIVE:
        result[PASSIVE_ID_TO_NAME[passiveId]] = passiveId

    for scytheId in ALL_SCYTHE:
        result[SCYTHE_ID_TO_NAME[scytheId]] = scytheId

    for consumeId in ALL_CONSUME:
        result[CONSUME_ID_TO_NAME[consumeId]] = consumeId

    result["City Map"] = MAP

    for mirrorId in ALL_MIRROR:
        result[MIRROR_ID_TO_NAME[mirrorId]] = mirrorId

    return result


def populate_item_pool(world: World, options: JunkoOptions):
    revolver = JunkoItem(ACTIVE_ID_TO_NAME[REVOLVER], ItemClass.progression, REVOLVER, world.player)
    world.multiworld.itempool.append(revolver)

    for i in range(6):
        baseball = JunkoItem(ACTIVE_ID_TO_NAME[BASEBALL], ItemClass.progression, BASEBALL, world.player)
        world.multiworld.itempool.append(baseball)

    for i in range(6):
        powder = JunkoItem(ACTIVE_ID_TO_NAME[POWDER], ItemClass.progression, POWDER, world.player)
        world.multiworld.itempool.append(powder)

    for i in range(6):
        drink = JunkoItem(ACTIVE_ID_TO_NAME[DRINK], ItemClass.progression, DRINK, world.player)
        world.multiworld.itempool.append(drink)

    pumpkin = JunkoItem(ACTIVE_ID_TO_NAME[PUMPKIN], ItemClass.progression, PUMPKIN, world.player)
    world.multiworld.itempool.append(pumpkin)

    hat = JunkoItem(ACTIVE_ID_TO_NAME[HAT], ItemClass.progression, HAT, world.player)
    world.multiworld.itempool.append(hat)

    fish = JunkoItem(ACTIVE_ID_TO_NAME[FISH], ItemClass.progression, FISH, world.player)
    world.multiworld.itempool.append(fish)

    sunflower = JunkoItem(ACTIVE_ID_TO_NAME[SUNFLOWER], ItemClass.progression, SUNFLOWER, world.player)
    world.multiworld.itempool.append(sunflower)

    phone = JunkoItem(ACTIVE_ID_TO_NAME[PHONE], ItemClass.progression, PHONE, world.player)
    world.multiworld.itempool.append(phone)

    ears = JunkoItem(ACTIVE_ID_TO_NAME[BEAR_CUB_EARS], ItemClass.progression, BEAR_CUB_EARS, world.player)
    world.multiworld.itempool.append(ears)

    for i in range(2):
        crown = JunkoItem(ACTIVE_ID_TO_NAME[CROWN], ItemClass.progression, CROWN, world.player)
        world.multiworld.itempool.append(crown)

    heart = JunkoItem(ACTIVE_ID_TO_NAME[HEART], ItemClass.progression, HEART, world.player)
    world.multiworld.itempool.append(heart)

    fig = JunkoItem(ACTIVE_ID_TO_NAME[FIG], ItemClass.progression, FIG, world.player)
    world.multiworld.itempool.append(fig)

    ice = JunkoItem(ACTIVE_ID_TO_NAME[ICE], ItemClass.progression, ICE, world.player)
    world.multiworld.itempool.append(ice)

    radsuit = JunkoItem(ACTIVE_ID_TO_NAME[RADSUIT], ItemClass.progression, RADSUIT, world.player)
    world.multiworld.itempool.append(radsuit)

    bone = JunkoItem(ACTIVE_ID_TO_NAME[BONE], ItemClass.progression, BONE, world.player)
    world.multiworld.itempool.append(bone)

    rat = JunkoItem(ACTIVE_ID_TO_NAME[RAT], ItemClass.progression, RAT, world.player)
    world.multiworld.itempool.append(rat)

    backpack = JunkoItem(ACTIVE_ID_TO_NAME[BACKPACK], ItemClass.progression, BACKPACK, world.player)
    world.multiworld.itempool.append(backpack)

    bell = JunkoItem(ACTIVE_ID_TO_NAME[BELL], ItemClass.useful, BELL, world.player)
    world.multiworld.itempool.append(bell)

    egg = JunkoItem(ACTIVE_ID_TO_NAME[EGG], ItemClass.progression, EGG, world.player)
    world.multiworld.itempool.append(egg)

    fiddle = JunkoItem(ACTIVE_ID_TO_NAME[FIDDLE], ItemClass.progression, FIDDLE, world.player)
    world.multiworld.itempool.append(fiddle)

    quill = JunkoItem(PASSIVE_ID_TO_NAME[QUILL], ItemClass.useful, QUILL, world.player)
    world.multiworld.itempool.append(quill)

    chest = JunkoItem(PASSIVE_ID_TO_NAME[CHEST], ItemClass.useful, CHEST, world.player)
    world.multiworld.itempool.append(chest)

    rocks = JunkoItem(PASSIVE_ID_TO_NAME[ROCKS], ItemClass.progression, ROCKS, world.player)
    if options.shuffle_strange_rocks:
        world.multiworld.itempool.append(rocks)
    else:
        world.multiworld.get_location(DEATH_ID_TO_NAME[DEATH_ROCKS], world.player).place_locked_item(rocks)

    rooster = JunkoItem(PASSIVE_ID_TO_NAME[ROOSTER], ItemClass.progression, ROOSTER, world.player)
    world.multiworld.itempool.append(rooster)

    ring = JunkoItem(PASSIVE_ID_TO_NAME[RING], ItemClass.progression, RING, world.player)
    world.multiworld.itempool.append(ring)

    lion_key = JunkoItem(PASSIVE_ID_TO_NAME[LION_KEY], ItemClass.progression, LION_KEY, world.player)
    world.multiworld.itempool.append(lion_key)

    handle = JunkoItem(SCYTHE_ID_TO_NAME[SCYTHE_HANDLE], ItemClass.progression, SCYTHE_HANDLE, world.player)
    world.multiworld.itempool.append(handle)

    blade = JunkoItem(SCYTHE_ID_TO_NAME[SCYTHE_BLADE], ItemClass.progression, SCYTHE_BLADE, world.player)
    world.multiworld.itempool.append(blade)

    for i in range(50):
        buttons = JunkoItem(CONSUME_ID_TO_NAME[FIVE_BUTTONS], ItemClass.filler, FIVE_BUTTONS, world.player)
        world.multiworld.itempool.append(buttons)

    for i in range(33):
        buttons = JunkoItem(CONSUME_ID_TO_NAME[TEN_BUTTONS], ItemClass.filler, TEN_BUTTONS, world.player)
        world.multiworld.itempool.append(buttons)

    for i in range(16):
        buttons = JunkoItem(CONSUME_ID_TO_NAME[TWENTY_FIVE_BUTTONS], ItemClass.progression,
                            TWENTY_FIVE_BUTTONS, world.player)
        world.multiworld.itempool.append(buttons)

    for i in range(1):
        buttons = JunkoItem(CONSUME_ID_TO_NAME[HUNDRED_BUTTONS], ItemClass.progression, HUNDRED_BUTTONS, world.player)
        world.multiworld.itempool.append(buttons)

    for i in range(12):
        key = JunkoItem(CONSUME_ID_TO_NAME[KEY], ItemClass.progression, KEY, world.player)
        world.multiworld.itempool.append(key)

    junkomap = JunkoItem("City Map", ItemClass.useful, MAP, world.player)
    world.multiworld.itempool.append(junkomap)

    jeans = JunkoItem(MIRROR_ID_TO_NAME[JEANS], ItemClass.filler, JEANS, world.player)
    world.multiworld.itempool.append(jeans)

    yukata = JunkoItem(MIRROR_ID_TO_NAME[YUKATA], ItemClass.filler, YUKATA, world.player)
    world.multiworld.itempool.append(yukata)

    stripes = JunkoItem(MIRROR_ID_TO_NAME[STRIPES], ItemClass.filler, STRIPES, world.player)
    world.multiworld.itempool.append(stripes)

    sailor = JunkoItem(MIRROR_ID_TO_NAME[SAILOR], ItemClass.filler, SAILOR, world.player)
    world.multiworld.itempool.append(sailor)

    sweater = JunkoItem(MIRROR_ID_TO_NAME[SWEATER], ItemClass.filler, SWEATER, world.player)
    world.multiworld.itempool.append(sweater)

    arcaust = JunkoItem(MIRROR_ID_TO_NAME[ARCAUST], ItemClass.filler, ARCAUST, world.player)
    world.multiworld.itempool.append(arcaust)

    checkers = JunkoItem(MIRROR_ID_TO_NAME[CHECKERS], ItemClass.filler, CHECKERS, world.player)
    world.multiworld.itempool.append(checkers)
