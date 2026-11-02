import typing
from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup
from .Items import action_item_data_table, omm_move_item_data_table, OMM_CAPTURE_BITS

class EnableCoinStars(Choice):
    """
    Determine logic for 100 Coin Stars.

    Off - Removed from pool. You can still collect them, but they don't do anything.
    Optimal for ignoring 100 Coin Stars entirely. Removes 15 locations from the pool.

    On - Kept in pool, potentially randomized.

    Vanilla - Kept in pool, but NOT randomized.
    """
    display_name = "Enable 100 Coin Stars"
    option_off = 0
    option_on = 1
    option_vanilla = 2

class StrictCapRequirements(DefaultOnToggle):
    """If disabled, Stars that expect special caps may have to be acquired without the caps"""
    display_name = "Strict Cap Requirements"


class StrictCannonRequirements(DefaultOnToggle):
    """If disabled, Stars that expect cannons may have to be acquired without them.
    Has no effect if Buddy Checks and Move Randomizer are disabled"""
    display_name = "Strict Cannon Requirements"


class FirstBowserStarDoorCost(Range):
    """What percent of the total stars are required at the Star Door to Bowser in the Dark World"""
    display_name = "First Star Door Cost %"
    range_start = 0
    range_end = 40
    default = 7


class BasementStarDoorCost(Range):
    """What percent of the total stars are required at the Star Door in the Basement"""
    display_name = "Basement Star Door %"
    range_start = 0
    range_end = 50
    default = 25


class SecondFloorStarDoorCost(Range):
    """What percent of the total stars are required to access the third floor"""
    display_name = 'Second Floor Star Door %'
    range_start = 0
    range_end = 70
    default = 42


class MIPS1Cost(Range):
    """What percent of the total stars are required to spawn MIPS the first time"""
    display_name = "MIPS 1 Star %"
    range_start = 0
    range_end = 35
    default = 12


class MIPS2Cost(Range):
    """What percent of the total stars are required to spawn MIPS the second time."""
    display_name = "MIPS 2 Star %"
    range_start = 0
    range_end = 70
    default = 42


class StarsToFinish(Range):
    """What percent of the total stars are required at the infinite stairs"""
    display_name = "Endless Stairs Star %"
    range_start = 0
    range_end = 90
    default = 58


class AmountOfStars(Range):
    """How many stars exist.
    If there aren't enough locations to hold the given total, the total will be reduced."""
    display_name = "Total Power Stars"
    range_start = 35
    range_end = 120
    default = 120


class AreaRandomizer(Choice):
    """Randomize Entrances"""
    display_name = "Entrance Randomizer"
    option_Off = 0
    option_Courses_Only = 1
    option_Courses_and_Secrets_Separate = 2
    option_Courses_and_Secrets = 3


class BuddyChecks(Toggle):
    """Bob-omb Buddies are checks, Cannon Unlocks are items"""
    display_name = "Bob-omb Buddy Checks"


class ExclamationBoxes(Toggle):
    """Include 1Up Exclamation Boxes during randomization.
    Adds 29 locations to the pool."""
    display_name = "Randomize 1Up !-Blocks"
    alias_1Ups_Only = 1


class CompletionType(Choice):
    """Set goal for game completion.

    Bowser 3 - Beat the last regular Bowser (Bowser in the Sky).

    All Vanilla Bowsers - Beat the three regular Bowsers: Dark World, Fire Sea and Sky.

    Pink-Gold Bowser - Beat the fourth Bowser, the Pink-Gold Sparkly Stars fight, to get its Grand Star.
    Needs Sparkly Stars enabled.

    Crystal Bowser - Beat the fifth Bowser, the Crystal Sparkly Stars fight, to get its Grand Star.
    Needs Sparkly Stars set to both modes.

    All Bowsers - Beat all five: the three regular Bowsers and both Sparkly Stars fights.
    Needs Sparkly Stars set to both modes."""
    display_name = "Completion Goal"
    option_Bowser_3 = 0
    option_All_Vanilla_Bowsers = 1
    option_Pink_Gold_Bowser = 2
    option_Crystal_Bowser = 3
    option_All_Bowsers = 4
    # Older names, kept so existing yamls still work
    alias_last_bowser_stage = 0
    alias_all_bowser_stages = 1
    alias_pink_gold_grand_star = 2
    alias_crystal_grand_star = 3
    alias_all_five_bowsers = 4


class ProgressiveKeys(DefaultOnToggle):
    """Keys will first grant you access to the Basement, then to the Second Floor"""
    display_name = "Progressive Keys"

class StrictMoveRequirements(DefaultOnToggle):
    """If disabled, Stars that expect certain moves may have to be acquired without them. Only makes a difference
    if Move Randomization is enabled"""
    display_name = "Strict Move Requirements"

class EnableMoveRandomizer(Toggle):
    """Mario is unable to perform some actions until a corresponding item is picked up.
    This option is incompatible with builds using a 'nomoverando' branch.
    Specific actions to randomize can be specified in the YAML."""
    display_name = "Enable Move Randomizer"

class MoveRandomizerActions(OptionSet):
    """Which actions to randomize when Move Randomizer is enabled"""
    display_name = "Randomized Moves"
    # HACK: Disable randomization for double jump
    valid_keys = [action for action in action_item_data_table if action != 'Double Jump']
    default = valid_keys

class EnableOmmMoveRandomizer(Toggle):
    """Mario is unable to use Odyssey Mario's Moveset moves (spin jump, roll, Cappy...) until a corresponding item is
    picked up. These items are never required to reach any location. The moves to randomize can be specified in the YAML."""
    display_name = "Enable OMM Move Randomizer"

class OmmMoveRandomizerActions(OptionSet):
    """Which OMM moves to randomize when the OMM Move Randomizer is enabled"""
    display_name = "Randomized OMM Moves"
    valid_keys = list(omm_move_item_data_table)
    default = valid_keys

class SparklyStars(Choice):
    """OMM's Sparkly Stars: post-game challenge stars that are checks, 30 per mode (29 challenge stars and the Grand Star
    of the fourth Bowser fight).
    Pink-Gold is the normal mode and Crystal is the hard one. Each mode is unlocked by an item ("Pink-Gold Stars",
    "Crystal Stars"), which makes its blocks appear in Castle Grounds. Since the challenges can need any move, they
    need all the randomized vanilla moves. The Pink-Gold Bowser and Crystal Bowser goals need their mode to be enabled. The \"All Bowsers\" goal (the three regular Bowsers
and both Grand Stars) needs both."""
    display_name = "Sparkly Stars"
    option_off = 0
    option_pink_gold = 1
    option_pink_gold_and_crystal = 2
    default = 0

class PinkGoldStarsForBowser(Range):
    """How many Pink-Gold Stars are needed before the fourth Bowser fight (the Pink-Gold Grand Star) opens.
    Only matters when Sparkly Stars is enabled. OMM's own rule is all 29."""
    display_name = "Pink-Gold Stars for Bowser 4"
    range_start = 1
    range_end = 29
    default = 29

class CrystalStarsForBowser(Range):
    """How many Crystal Stars are needed before the fifth Bowser fight (the Crystal Grand Star) opens.
    Only matters when both Sparkly Stars modes are enabled. OMM's own rule is all 29."""
    display_name = "Crystal Stars for Bowser 5"
    range_start = 1
    range_end = 29
    default = 29

class DisableToadCapture(DefaultOnToggle):
    """A captured Toad can walk through star doors, skipping their star requirement, which breaks logic.
    When enabled, the Toad capture is disabled and no item is created for it. Disable this option to treat Toad like any other capture."""
    display_name = "Disable Toad Capture"

class EnableCaptureRandomizer(Toggle):
    """Mario is unable to capture an enemy type until the corresponding item is picked up.
    These items are never required to reach any location. They take the place of 1Up Mushrooms first (OMM has no
    lives); if there aren't enough of those, the total number of Power Stars is reduced to make room."""
    display_name = "Enable Capture Randomizer"

class CaptureRandomizerCaptures(OptionSet):
    """Which enemy types to randomize when the Capture Randomizer is enabled"""
    display_name = "Randomized Captures"
    valid_keys = list(OMM_CAPTURE_BITS)
    default = valid_keys

sm64_options_groups = [
    OptionGroup("Logic Options", [
        AreaRandomizer,
        BuddyChecks,
        ExclamationBoxes,
        ProgressiveKeys,
        EnableCoinStars,
        StrictCapRequirements,
        StrictCannonRequirements,
    ]),
    OptionGroup("Ability Options", [
        EnableMoveRandomizer,
        MoveRandomizerActions,
        StrictMoveRequirements,
    ]),
    OptionGroup("OMM Options", [
        EnableOmmMoveRandomizer,
        OmmMoveRandomizerActions,
        EnableCaptureRandomizer,
        CaptureRandomizerCaptures,
        DisableToadCapture,
        SparklyStars,
        PinkGoldStarsForBowser,
        CrystalStarsForBowser,
    ]),
    OptionGroup("Star Options", [
        AmountOfStars,
        FirstBowserStarDoorCost,
        BasementStarDoorCost,
        SecondFloorStarDoorCost,
        MIPS1Cost,
        MIPS2Cost,
        StarsToFinish,
    ]),
]

@dataclass
class SM64Options(PerGameCommonOptions):
    area_rando: AreaRandomizer
    buddy_checks: BuddyChecks
    exclamation_boxes: ExclamationBoxes
    progressive_keys: ProgressiveKeys
    enable_coin_stars: EnableCoinStars
    enable_move_rando: EnableMoveRandomizer
    move_rando_actions: MoveRandomizerActions
    enable_omm_move_rando: EnableOmmMoveRandomizer
    omm_move_rando_actions: OmmMoveRandomizerActions
    enable_capture_rando: EnableCaptureRandomizer
    capture_rando_captures: CaptureRandomizerCaptures
    disable_toad_capture: DisableToadCapture
    sparkly_stars: SparklyStars
    pink_gold_stars_for_bowser: PinkGoldStarsForBowser
    crystal_stars_for_bowser: CrystalStarsForBowser
    strict_cap_requirements: StrictCapRequirements
    strict_cannon_requirements: StrictCannonRequirements
    strict_move_requirements: StrictMoveRequirements
    amount_of_stars: AmountOfStars
    first_bowser_star_door_cost: FirstBowserStarDoorCost
    basement_star_door_cost: BasementStarDoorCost
    second_floor_star_door_cost: SecondFloorStarDoorCost
    mips1_cost: MIPS1Cost
    mips2_cost: MIPS2Cost
    stars_to_finish: StarsToFinish
    death_link: DeathLink
    completion_type: CompletionType
