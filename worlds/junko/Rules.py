from BaseClasses import MultiWorld, CollectionState
from ..generic.Rules import add_rule
from .Items import *
from .Locations import *


def set_rules(multiworld: MultiWorld, world, player: int):
    multiworld.completion_condition[player] = lambda state: (
            state.can_reach("Memory Lane", player=player) and state.has(PASSIVE_ID_TO_NAME[LION_KEY], player) and
            state.has(PASSIVE_ID_TO_NAME[ROCKS], world.player)
    )

    loc = multiworld.get_location(APT_ID_TO_NAME[APT_BEDROOM_KEY], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player))

    loc = multiworld.get_location(APT_ID_TO_NAME[APT_HALLWAY_LION_BUTTON], player)
    add_rule(loc, lambda state: state.has(PASSIVE_ID_TO_NAME[LION_KEY], player))

    # Shops
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_MAP], player)
    add_rule(loc, lambda state: can_buy(state, player, 300))
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_SHOP_KEY], player)
    add_rule(loc, lambda state: can_buy(state, player, 300))
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_SHOP_BASEBALL], player)
    add_rule(loc, lambda state: can_buy(state, player, 300))
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_SHOP_POWDER], player)
    add_rule(loc, lambda state: can_buy(state, player, 300))
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_SHOP_DRINK], player)
    add_rule(loc, lambda state: can_buy(state, player, 300))

    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_CHEST], player)
    add_rule(loc, lambda state: can_buy(state, player, 400) and state.has(PASSIVE_ID_TO_NAME[LION_KEY], player))

    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_RAT_CLOAK], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[HAT], player) and
             (
                     can_fly(state, player) or
                     state.has(ACTIVE_ID_TO_NAME[BASEBALL], player) or state.has(ACTIVE_ID_TO_NAME[FISH], player)
             )
             )
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_RAT_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[HAT], player) and
             (
                     can_fly(state, player) or
                     state.has(ACTIVE_ID_TO_NAME[BASEBALL], player) or state.has(ACTIVE_ID_TO_NAME[FISH], player)
             ) and
             state.has(ACTIVE_ID_TO_NAME[RAT], player)
             )
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_RAT_BASEBALL], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[HAT], player) and
             (
                     can_fly(state, player) or
                     state.has(ACTIVE_ID_TO_NAME[BASEBALL], player) or state.has(ACTIVE_ID_TO_NAME[FISH], player)
             ) and
             (
                     state.has(ACTIVE_ID_TO_NAME[RAT], player) or state.has(ACTIVE_ID_TO_NAME[BASEBALL], player)
             )
             )

    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_CELLS_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_CELLS_POWDER], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_GAP_DRINK], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[DRINK], player) or can_fly(state, player))

    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_GATE_POWDER], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BASEBALL], player) or can_fly(state, player))
    loc = multiworld.get_location(INSIDES_ID_TO_NAME[INSIDES_GATE_CRACK_BUTTON], player)
    add_rule(loc,
             lambda state:
             (state.has(ACTIVE_ID_TO_NAME[BASEBALL], player) or can_fly(state, player))
             and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )

    loc = multiworld.get_location(RADIO_ID_TO_NAME[RADIO_CRACK_DRINK], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[DRINK], player))

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PARLOR_HIDDEN_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[DRINK], player) and state.has(ACTIVE_ID_TO_NAME[POWDER], player)
             )

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PIT_MAZE_BASEBALL], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player))
    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PIT_MAZE_LEFT_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player))
    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PIT_MAZE_RIGHT_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player))
    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PIT_MAZE_TOP_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player) and can_fly(state, player))

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_HOLES_ISOLATED_BUTTON], player)
    add_rule(loc, lambda state: can_fly(state, player))

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PANPON_HIDDEN_BUTTON], player)
    add_rule(loc, lambda state: can_fly(state, player))
    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_PANPON_MIRROR], player)
    add_rule(loc, lambda state: can_fly(state, player))

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_HIDDEN_CRACK_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[DRINK], player) and state.has(ACTIVE_ID_TO_NAME[POWDER], player)
             )

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_ILLUSION_BUTTON], player)
    add_rule(loc, lambda state: state.has(PASSIVE_ID_TO_NAME[RING], player))
    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_ILLUSION_KEY], player)
    add_rule(loc, lambda state: state.has(PASSIVE_ID_TO_NAME[RING], player))
    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_ILLUSION_DRINK], player)
    add_rule(loc,
             lambda state:
             state.has(PASSIVE_ID_TO_NAME[RING], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )

    loc = multiworld.get_location(SECOND_ID_TO_NAME[SECOND_MIRROR], player)
    add_rule(loc,
             lambda state:
             (can_unlock(state, player) or state.has(ACTIVE_ID_TO_NAME[PHONE], player)) and
             state.has(ACTIVE_ID_TO_NAME[FISH], player) and state.has(ACTIVE_ID_TO_NAME[RAT], player)
             )

    loc = multiworld.get_location(ALLEY_ID_TO_NAME[ALLEY_PUMPKIN], player)
    add_rule(loc, lambda state: can_unlock(state, player))

    loc = multiworld.get_location(ALLEY_ID_TO_NAME[ALLEY_CRACKED_LEFT_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[DRINK], player))
    loc = multiworld.get_location(ALLEY_ID_TO_NAME[ALLEY_CRACKED_RIGHT_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[DRINK], player))

    loc = multiworld.get_location(FIELD_ID_TO_NAME[FIELD_PATH_DIG_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(FIELD_ID_TO_NAME[FIELD_FENCE_DIG_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[BONE], player) and
             (state.has(PASSIVE_ID_TO_NAME[RING], player) or state.has(PASSIVE_ID_TO_NAME[ROOSTER], world.player))
             )
    loc = multiworld.get_location(FIELD_ID_TO_NAME[FIELD_GRASS_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[HAT], player) and
             (state.has(PASSIVE_ID_TO_NAME[RING], player) or state.has(PASSIVE_ID_TO_NAME[ROOSTER], world.player))
             )
    loc = multiworld.get_location(FIELD_ID_TO_NAME[FIELD_GRASS_DIG_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[BONE], player) and
             (state.has(PASSIVE_ID_TO_NAME[RING], player) or state.has(PASSIVE_ID_TO_NAME[ROOSTER], world.player))
             )

    loc = multiworld.get_location(FIELD_ID_TO_NAME[FIELD_HAT], player)
    add_rule(loc,
             lambda state:
             (
                     (state.has(PASSIVE_ID_TO_NAME[RING], player) and can_unlock(state, player))
                     or state.has(PASSIVE_ID_TO_NAME[ROOSTER], world.player)
             ) and
             (state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player))
             )

    loc = multiworld.get_location(FIELD_ID_TO_NAME[FIELD_POWDER], player)
    add_rule(loc,
             lambda state:
             state.has(PASSIVE_ID_TO_NAME[RING], player) or state.has(PASSIVE_ID_TO_NAME[ROOSTER], world.player))

    loc = multiworld.get_location(WOODS_ID_TO_NAME[WOODS_FESTIVAL_DIG_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_DIG_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_SALOON_BASEMENT_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[DRINK], player))

    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_SALOON_ROOM_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player))

    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_FLG_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_BLG_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_BRG_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_FRG_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_LB_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_MB_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_RB_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_CAVE_P_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )

    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_HOT_FENCE_BUTTON], player)
    add_rule(loc, lambda state: can_desert(state, player))
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_HOT_GREY_BUTTON], player)
    add_rule(loc, lambda state: can_desert(state, player))
    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_HOT_RUINS_BUTTON], player)
    add_rule(loc, lambda state: can_desert(state, player))

    loc = multiworld.get_location(SANDS_ID_TO_NAME[SANDS_HOT_BONE], player)
    add_rule(loc,
             lambda state:
             (can_desert(state, player) and state.has(ACTIVE_ID_TO_NAME[PUMPKIN], player)) or
             state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_SPRINGS_BUTTON], player)
    add_rule(loc, lambda state: can_fly(state, player))

    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_CROWN], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player))
    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_BAR_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player) and can_fly(state, player))

    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_FREEZER_VOID_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player))
    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_FREEZER_ICE], player)
    add_rule(loc,
             lambda state:
             can_unlock(state, player) and state.has(ACTIVE_ID_TO_NAME[HAT], player)  # TODO FISH?
             )

    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_MINES_G_BUTTON], player)
    add_rule(loc,
             lambda state:
             can_fly(state, player) or
             state.has(ACTIVE_ID_TO_NAME[RAT], player) or state.has(ACTIVE_ID_TO_NAME[POWDER], player)
             )
    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_MINES_B_BUTTON], player)
    add_rule(loc,
             lambda state:
             can_fly(state, player) or
             state.has(ACTIVE_ID_TO_NAME[RAT], player) or state.has(ACTIVE_ID_TO_NAME[POWDER], player)
             )
    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_MINES_CABIN_BUTTON], player)
    add_rule(loc,
             lambda state:
             can_fly(state, player) or
             state.has(ACTIVE_ID_TO_NAME[RAT], player) or state.has(ACTIVE_ID_TO_NAME[POWDER], player)
             )
    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_CABIN_FISH], player)
    add_rule(loc,
             lambda state:
             can_fly(state, player) or
             state.has(ACTIVE_ID_TO_NAME[RAT], player) or state.has(ACTIVE_ID_TO_NAME[POWDER], player)
             )
    loc = multiworld.get_location(SNOW_ID_TO_NAME[SNOW_MINES_MIRROR], player)
    add_rule(loc, lambda state: can_fly(state, player))

    loc = multiworld.get_location(FIRST_ID_TO_NAME[FIRST_DIG_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(FIRST_ID_TO_NAME[FIRST_GARAGE_POWDER], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[RAT], player))

    loc = multiworld.get_location(FIRST_ID_TO_NAME[FIRST_GARAGE_MIRROR], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[RAT], player) and
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )

    loc = multiworld.get_location(FIRST_ID_TO_NAME[FIRST_HEART_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BEAR_CUB_EARS], player))
    loc = multiworld.get_location(FIRST_ID_TO_NAME[FIRST_HEART_EGG], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[BEAR_CUB_EARS], player) and state.has(ACTIVE_ID_TO_NAME[HEART], player)
             )

    loc = multiworld.get_location(RAVE_ID_TO_NAME[RAVE_DIG_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))
    loc = multiworld.get_location(RAVE_ID_TO_NAME[RAVE_GRAVE_DRINK], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], player))

    loc = multiworld.get_location(SHEOL_ID_TO_NAME[SHEOL_CRYPT_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[EGG], player))

    loc = multiworld.get_location(THIRD_ID_TO_NAME[THIRD_ABANDON_BASEBALL], player)
    add_rule(loc, lambda state: can_unlock(state, player))
    loc = multiworld.get_location(THIRD_ID_TO_NAME[THIRD_ABANDON_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player))

    loc = multiworld.get_location(THIRD_ID_TO_NAME[THIRD_ABANDON_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[DRINK], player))

    loc = multiworld.get_location(THIRD_ID_TO_NAME[THIRD_PERVERT_BUTTON], player)
    add_rule(loc,
             lambda state:
             state.has(ACTIVE_ID_TO_NAME[DRINK], player) and state.has(ACTIVE_ID_TO_NAME[POWDER], player) and
             can_fly(state, player)
             )

    loc = multiworld.get_location(CANAL_ID_TO_NAME[CANAL_PUMPKIN_BUTTON], player)
    add_rule(loc, lambda state: can_fly(state, player) or state.has(ACTIVE_ID_TO_NAME[ICE], player))
    loc = multiworld.get_location(CANAL_ID_TO_NAME[CANAL_DOWNSTAIRS_BUTTON], player)
    add_rule(loc, lambda state: can_fly(state, player) or state.has(ACTIVE_ID_TO_NAME[ICE], player))
    loc = multiworld.get_location(CANAL_ID_TO_NAME[CANAL_ELEVATOR_BASEBALL], player)
    add_rule(loc, lambda state: can_fly(state, player) or state.has(ACTIVE_ID_TO_NAME[ICE], player))
    loc = multiworld.get_location(CANAL_ID_TO_NAME[CANAL_CROWN_ENCHANT], player)
    add_rule(loc,
             lambda state:
             can_fly(state, player) or state.has(ACTIVE_ID_TO_NAME[ICE], player) and
             state.has(ACTIVE_ID_TO_NAME[BASEBALL], player)
             )

    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_CLUB_HIDDEN_BUTTON], player)
    add_rule(loc,
             lambda state:
             can_unlock(state, player) and
             state.has(ACTIVE_ID_TO_NAME[POWDER], player) and state.has(ACTIVE_ID_TO_NAME[DRINK], player)
             )
    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_DESERT_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player))
    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_DESERT_MIRROR], player)
    add_rule(loc, lambda state: can_unlock(state, player))
    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_DESERT_POWDER], player)
    add_rule(loc, lambda state: can_unlock(state, player) and state.has(ACTIVE_ID_TO_NAME[POWDER], player))
    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_DESERT_RADSUIT], player)
    add_rule(loc, lambda state: can_unlock(state, player) and state.has(ACTIVE_ID_TO_NAME[POWDER], player))

    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_HUNTER_ROOSTER], player)
    add_rule(loc, lambda state: can_unlock(state, player))
    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_HUNTER_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player))

    loc = multiworld.get_location(FOURTH_ID_TO_NAME[FOURTH_HOSPITAL_HEART], player)
    add_rule(loc, lambda state: can_unlock(state, player))

    loc = multiworld.get_location(FIFTH_ID_TO_NAME[FIFTH_DIG_BUTTON], player)
    add_rule(loc, lambda state: state.has(ACTIVE_ID_TO_NAME[BONE], world.player))

    loc = multiworld.get_location(FIFTH_ID_TO_NAME[FIFTH_APT_REFILL_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player))

    loc = multiworld.get_location(FIFTH_ID_TO_NAME[FIFTH_HYPNO_BUTTON], player)
    add_rule(loc, lambda state: can_unlock(state, player))
    loc = multiworld.get_location(FIFTH_ID_TO_NAME[FIFTH_HYPNO_EARS], player)
    add_rule(loc, lambda state: can_unlock(state, player) and state.has(ACTIVE_ID_TO_NAME[BONE], world.player))


def can_buy(state: CollectionState, player, amount: int):
    # TODO spider grinding logic options
    buttons = (
            (state.count(CONSUME_ID_TO_NAME[TWENTY_FIVE_BUTTONS], player) * 25) +
            (state.count(CONSUME_ID_TO_NAME[HUNDRED_BUTTONS], player) * 100)
    )
    return buttons >= amount


def can_fly(state: CollectionState, player):
    return state.has(ACTIVE_ID_TO_NAME[CROWN], player, 2)


def can_unlock(state: CollectionState, player):
    return state.has(PASSIVE_ID_TO_NAME[LION_KEY], player) or state.has(CONSUME_ID_TO_NAME[KEY], player, 12)


def can_desert(state: CollectionState, player):
    return state.has(ACTIVE_ID_TO_NAME[ICE], player) or state.has(ACTIVE_ID_TO_NAME[FIG], player)
