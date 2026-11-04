from typing import NamedTuple

from BaseClasses import Item, ItemClassification

sm64ex_base_id: int = 3626000

class SM64Item(Item):
    game: str = "Super Mario 64 OMM"

class SM64ItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression

generic_item_data_table: dict[str, SM64ItemData] = {
    "Power Star": SM64ItemData(sm64ex_base_id + 0, ItemClassification.progression_deprioritized_skip_balancing),
    "Basement Key": SM64ItemData(sm64ex_base_id + 178),
    "Second Floor Key": SM64ItemData(sm64ex_base_id + 179),
    "Progressive Key": SM64ItemData(sm64ex_base_id + 180),
    "Wing Cap": SM64ItemData(sm64ex_base_id + 181),
    "Metal Cap": SM64ItemData(sm64ex_base_id + 182),
    "Vanish Cap": SM64ItemData(sm64ex_base_id + 183),
    "1Up Mushroom": SM64ItemData(sm64ex_base_id + 184, ItemClassification.filler),
}

action_item_data_table: dict[str, SM64ItemData] = {
    "Double Jump": SM64ItemData(sm64ex_base_id + 185),
    "Triple Jump": SM64ItemData(sm64ex_base_id + 186),
    "Long Jump": SM64ItemData(sm64ex_base_id + 187),
    "Backflip": SM64ItemData(sm64ex_base_id + 188),
    "Side Flip": SM64ItemData(sm64ex_base_id + 189),
    "Wall Kick": SM64ItemData(sm64ex_base_id + 190),
    "Dive": SM64ItemData(sm64ex_base_id + 191),
    "Ground Pound": SM64ItemData(sm64ex_base_id + 192),
    "Kick": SM64ItemData(sm64ex_base_id + 193),
    "Climb": SM64ItemData(sm64ex_base_id + 194),
    "Ledge Grab": SM64ItemData(sm64ex_base_id + 195),
}

cannon_item_data_table: dict[str, SM64ItemData] = {
    "Cannon Unlock BoB": SM64ItemData(sm64ex_base_id + 200),
    "Cannon Unlock WF": SM64ItemData(sm64ex_base_id + 201),
    "Cannon Unlock JRB": SM64ItemData(sm64ex_base_id + 202),
    "Cannon Unlock CCM": SM64ItemData(sm64ex_base_id + 203),
    "Cannon Unlock SSL": SM64ItemData(sm64ex_base_id + 207),
    "Cannon Unlock SL": SM64ItemData(sm64ex_base_id + 209),
    "Cannon Unlock WDW": SM64ItemData(sm64ex_base_id + 210),
    "Cannon Unlock TTM": SM64ItemData(sm64ex_base_id + 211),
    "Cannon Unlock THI": SM64ItemData(sm64ex_base_id + 212),
    "Cannon Unlock RR": SM64ItemData(sm64ex_base_id + 214),
}

# --- Odyssey Mario's Moveset ---
# These IDs must match the game build (SM64AP_OMM_MOVE_OFFSET / SM64AP_OMM_CAPTURE_OFFSET in sm64ap.h).
# They are not required by logic, except "Cappy Throw" and "Capture Bob-omb" when they are randomized: every Bowser
# fight of OMM needs them.

omm_move_item_data_table: dict[str, SM64ItemData] = {
    "Spin Jump": SM64ItemData(sm64ex_base_id + 400, ItemClassification.useful),
    "Midair Spin": SM64ItemData(sm64ex_base_id + 401, ItemClassification.useful),
    "Roll": SM64ItemData(sm64ex_base_id + 402, ItemClassification.useful),
    "Cappy Throw": SM64ItemData(sm64ex_base_id + 403, ItemClassification.useful),
    "Cappy Bounce": SM64ItemData(sm64ex_base_id + 404, ItemClassification.useful),
    "Cappy Vault": SM64ItemData(sm64ex_base_id + 405, ItemClassification.useful),
    "Water Dash": SM64ItemData(sm64ex_base_id + 406, ItemClassification.useful),
}
# The spin pound is unlocked by the vanilla "Ground Pound" item and the wall slide by "Wall Kick":
# in OMM they are the same move, and the logic requires those two items.

# One item per enemy type. The number is OMM's capture bit index (OMM_CAPTURE_* in omm_capture_all.h), and
# variants of the same enemy share one item: Goomba (incl. huge/tiny), Koopa (incl. shells), Bob-omb (incl.
# flaming), Bob-omb Buddy (incl. cannon), Ukiki (hat and cage).
OMM_CAPTURE_BITS: dict[str, int] = {
    "Goomba": 0, "Koopa": 3, "Bob-omb": 6, "Bob-omb Buddy": 7, "Chain Chomp": 9, "Bullet Bill": 10, "Hoot": 11,
    "Whomp": 12, "Thwomp": 13, "Spindrift": 14, "Small Penguin": 15, "Mr. Blizzard": 16, "Snowman": 17, "Boo": 18,
    "Big Boo": 19, "Scuttlebug": 20, "Mad Piano": 21, "Crazy Box": 22, "Mr. I": 23, "Swoop": 24, "Snufit": 25,
    "Monty Mole": 26, "Dorrie": 27, "Bully": 28, "Fly Guy": 29, "Pokey": 30, "Amp": 31, "Grindel": 32,
    "Fire Spitter": 33, "Cheep Cheep": 34, "Sushi": 35, "Moneybag": 36, "Skeeter": 37, "Heave-Ho": 38,
    "Chuckya": 39, "Ukiki": 40, "Lakitu": 42, "Spiny": 43, "Toad": 44, "MIPS": 45, "Yoshi": 47,
}

omm_capture_item_data_table: dict[str, SM64ItemData] = {
    f"Capture {name}": SM64ItemData(sm64ex_base_id + 500 + bit, ItemClassification.useful)
    for name, bit in OMM_CAPTURE_BITS.items()
}

# Sparkly Stars modes (see Sparkly.py): each item makes the blocks of its mode appear in Castle Grounds
sparkly_item_data_table: dict[str, SM64ItemData] = {
    "Pink-Gold Stars": SM64ItemData(sm64ex_base_id + 450),
    "Crystal Stars": SM64ItemData(sm64ex_base_id + 451),
}

item_data_table = {
    **generic_item_data_table,
    **action_item_data_table,
    **cannon_item_data_table,
    **omm_move_item_data_table,
    **omm_capture_item_data_table,
    **sparkly_item_data_table,
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
