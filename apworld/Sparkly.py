"""OMM's Sparkly Stars: post-game challenge stars, one set per mode (Pink-Gold = Normal, Crystal = Hard).

Each mode has 29 challenge stars (one per course, secret level and castle area), then the fourth Bowser fight
(which unlocks once enough of the 29 stars are collected, 29 by default), whose Grand Star is the last check: 30 checks per mode.
A mode is unlocked by an item ("Pink-Gold Stars" / "Crystal Stars"), which makes its blocks appear in Castle Grounds.
The numbers here must match the game: OMM's sparkly star index (omm_sparkly_data.c) and SM64AP_LOCATIONID_SPARKLY."""
from .Items import sm64ex_base_id

SPARKLY_LOCATION_BASE: int = sm64ex_base_id + 600
SPARKLY_STRIDE: int = 40  # location IDs per mode

# Mode name, index (OMM mode = index + 1), unlock item
SPARKLY_MODES: dict[str, tuple[int, str]] = {
    "Pink-Gold": (0, "Pink-Gold Stars"),
    "Crystal": (1, "Crystal Stars"),
}

# Challenge stars in OMM's order (the index is the star index), with the region they are played in
SPARKLY_STARS: list[tuple[str, str]] = [
    ("BoB", "Bob-omb Battlefield"), ("WF", "Whomp's Fortress"), ("JRB", "Jolly Roger Bay"),
    ("CCM", "Cool, Cool Mountain"), ("BBH", "Big Boo's Haunt"), ("HMC", "Hazy Maze Cave"),
    ("LLL", "Lethal Lava Land"), ("SSL", "Shifting Sand Land"), ("DDD", "Dire, Dire Docks"),
    ("SL", "Snowman's Land"), ("WDW", "Wet-Dry World"), ("TTM", "Tall, Tall Mountain"),
    ("THI", "Tiny-Huge Island"), ("TTC", "Tick Tock Clock"), ("RR", "Rainbow Ride"),
    ("BitDW", "Bowser in the Dark World"), ("BitFS", "Bowser in the Fire Sea"), ("BitS", "Bowser in the Sky"),
    ("TotWC", "Tower of the Wing Cap"), ("VCutM", "Vanish Cap under the Moat"), ("CotMC", "Cavern of the Metal Cap"),
    ("PSS", "The Princess's Secret Slide"), ("WMotR", "Wing Mario over the Rainbow"), ("SA", "The Secret Aquarium"),
    ("Castle Grounds", "Menu"), ("Castle Lobby", "Menu"), ("Castle Basement", "Basement"),
    ("Castle Upstairs", "Second Floor"), ("Castle Courtyard", "Menu"),
]
NUM_CHALLENGE_STARS: int = len(SPARKLY_STARS)  # 29
GRAND_STAR: str = "Grand Star"    # given by the fourth Bowser fight, in Castle Grounds
LOCATIONS_PER_MODE: int = NUM_CHALLENGE_STARS + 1

# Spot name, region, for every location of a mode, in ID order (the Grand Star has index 29)
_SPOTS: list[tuple[str, str]] = SPARKLY_STARS + [(GRAND_STAR, "Menu")]


def sparkly_location_name(mode: str, spot: str) -> str:
    return f"{mode}: {spot}"


sparkly_location_table: dict[str, int] = {
    sparkly_location_name(mode, spot): SPARKLY_LOCATION_BASE + SPARKLY_STRIDE * index + i
    for mode, (index, _item) in SPARKLY_MODES.items()
    for i, (spot, _region) in enumerate(_SPOTS)
}


def enabled_sparkly_modes(options) -> list[str]:
    """The modes in the seed: none, Pink-Gold, or both."""
    count = options.sparkly_stars.value
    return list(SPARKLY_MODES)[:count]


def sparkly_modes_bitmask(options) -> int:
    return sum(1 << SPARKLY_MODES[mode][0] for mode in enabled_sparkly_modes(options))


def create_sparkly_locations(multiworld, options, player):
    from .Locations import SM64Location  # imported here: Locations imports this module for its table
    for mode in enabled_sparkly_modes(options):
        for spot, region_name in _SPOTS:
            region = multiworld.get_region(region_name, player)
            name = sparkly_location_name(mode, spot)
            region.locations.append(SM64Location(player, name, sparkly_location_table[name], region))


def set_sparkly_rules(multiworld, options, player):
    from ..generic.Rules import set_rule
    from .Items import action_item_data_table
    modes = enabled_sparkly_modes(options)

    # The challenges can need any move, so they ask for all the randomized ones: this keeps them from
    # being placed in a way that would lock a move behind a challenge that needs that move.
    needed_moves = []
    if options.enable_move_rando:
        needed_moves = [move for move in options.move_rando_actions.value if move in action_item_data_table]

    for mode in modes:
        unlock_item = SPARKLY_MODES[mode][1]
        stars = [sparkly_location_name(mode, spot) for spot, _region in SPARKLY_STARS]

        def can_play(state, unlock_item=unlock_item):
            return state.has(unlock_item, player) and state.has_all(needed_moves, player)

        for name in stars:
            set_rule(multiworld.get_location(name, player), can_play)

        # The fight opens with the configured number of stars, and the Grand Star comes from that fight
        required = (options.pink_gold_stars_for_bowser if mode == "Pink-Gold" else options.crystal_stars_for_bowser).value

        def can_fight_bowser(state, stars=stars, can_play=can_play, required=required):
            return can_play(state) and sum(1 for star in stars if state.can_reach(star, "Location", player)) >= required

        set_rule(multiworld.get_location(sparkly_location_name(mode, GRAND_STAR), player), can_fight_bowser)

    # Goals: collect the Grand Star of a mode
    goal_modes = {2: "Pink-Gold", 3: "Crystal"}
    goal_mode = goal_modes.get(options.completion_type.value)
    if goal_mode:
        goal_location = sparkly_location_name(goal_mode, GRAND_STAR)
        multiworld.completion_condition[player] = lambda state: state.can_reach(goal_location, "Location", player)

    # All Five Bowsers: the three regular Bowser stages, then both fights of the Sparkly Stars modes
    if options.completion_type.value == 4:
        grand_stars = [sparkly_location_name(mode, GRAND_STAR) for mode in modes]
        multiworld.completion_condition[player] = lambda state: (
            state.can_reach("Bowser in the Dark World", "Region", player)
            and state.can_reach("BitFS: Upper", "Region", player)
            and state.can_reach("BitS: Top", "Region", player)
            and all(state.can_reach(grand_star, "Location", player) for grand_star in grand_stars))
