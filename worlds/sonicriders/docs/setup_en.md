# Sonic Riders Setup Guide

## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases)
- Dolphin Emulator, recommended 2409 version of higher.
- An NTSC Rom for Sonic Riders for Gamecube. The Archipelago community cannot provide this.


### Configuring Game

- Launch Dolphin, go to options - configuration - interface and tick Enable Debugging UI
- Download the Python Dolphin Memory engine, and install into the lib folder of your Archipelago folder. 
- Disable use of Emulated Memory Size override, as archipelago will not work with this setting.

## Optional Software
- Universal Tracker: This game aims to support universal tracker allowing you to know what checks are available in game.

## Generating a Game
1. Create your options file (YAML). Refer to the generated file for information regarding the options. 
	If you want the latest template, open the Archipelago Launcher and click 'Generate Templates'
2. Follow the general Archipelago instructions for [generating a game](../../Archipelago/setup/en#generating-a-game).
   This will generate an output file.
3. Open `ArchipelagoLauncher.exe`
4. Host your game. You can host local games using 'Host' option on the launcher, or upload to Archipelago's site.
5. Open Dolphin emulator. 
6. Open the Sonic Riders rom.
7. Select 'Sonic Riders Client' in Archipelago Launcher.
8. Enter your credentials and connect to the server.
9. Make a new save.
10.  Play!

You must remain with client running whenever playing the game to receive checks and other items.
You should now be able to receive and send items. You'll need to do these steps every time you want to reconnect.