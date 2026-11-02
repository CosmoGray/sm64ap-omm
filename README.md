# Odyssey Mario's Moveset Archipelago
A fork of SM64EX-OMM that works with Archipelago Multiworlds

The game will literally not let you play unless you're connected to an Archipelago Multiworld Randomizer. If you want to play Odyssey Mario's Moveset on its own, please download the game from [PeachyPeach's Odyssey Mario Moveset SM64EX repo](https://github.com/PeachyPeachSM64/sm64ex-omm).

# About & Credits
AP Implementation based on [N00byKing's SM64EX](https://github.com/N00byKing/sm64ex) as well as [the launcher](https://github.com/N00byKing/SM64AP-Launcher), this patch lets you connect to Archipelago in-game rather than going through a launcher.

Full credits for Odyssey Mario's Moveset can be found in [its repo](https://github.com/PeachyPeachSM64/sm64ex-omm), special thanks to PeachyPeach for her permission to make this.

# New YAML Options
These are the yaml options that are new to sm64ap-omm, there are more not listed that are derived from N00byKing's sm64ex AP. All descriptions are what happens when true unless specified.

*As this is a mod of SM64 and has all of the normal SM64 levels, none of these moves are in logic as required for any star.*

enable-omm-move-rando - Randomizes the following moves into logic:
- Cappy Throw
- Cappy Bounce
- Cappy Vault
- Midair Spin
- Roll
- Spin Jump
- Water Dash

enable-capture-rando - Randomizes all captures into logic. Once again, none required for any star.

disable-toad-capture - Disables the Toad capture, which allows you to bypass star or key door requirements.

sparkly-stars - Options: 'off', 'pink_gold', 'pink_gold_and_crystal'. Enables post-game challenge stars, 30 extra checks per mode. 60 total if pink_gold_and_crystal is enabled.

pink_gold_stars_for_bowser - Normally 29, you can set this to not require collecting every Pink Gold Star before the Pink Gold Bowser Fight. Minimum is 1.

crystal_stars_for_bowser - Normally 29, you can set this to not require collecting every Crystal Star before the Pink Gold Bowser Fight. Minimum is 1.

# How to play
This can be found in the Readme of the release as well.

1. You can find the apworld and a test YAML in the "Archipelago" folder in the same directory as this readme. Make sure your host has installed the apworld before generating.
2. Place a legally obtained US ROM of Super Mario 64 in the same directory as "sm64.smex.exe" (In the "Game" folder)
3. Open the game
4. Once your Archipelago is being hosted, use your controller to select the "Archipelago" option at the bottom of the main menu
5. Select the fields and use your keyboard to input the correct information to connect, then press "Connect"
6. You can select a file in the "Play" menu, but I prefer pressing the Start button to skip the intro cutscene on "Play without saving." The apworld will load what you've already gotten.
