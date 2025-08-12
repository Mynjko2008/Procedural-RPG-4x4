# Procedural RPG 4x4

A simple procedural-generated dungeon crawler RPG implemented in Python.

## Overview

This is a text-based RPG game featuring a 4x4 grid map with randomly generated rooms.  
The player's objective is to explore the dungeon, find the rare sword (treasure), and then reach the exit to win the game.

The map contains different room types:

- **Empty rooms** (unknown)
- **Enemy rooms** with turn-based combat
- **Item rooms** with random pickups and buffs
- **Treasure room** containing the rare sword
- **Exit room** where the player escapes after finding the sword

## Gameplay

- The player starts at position (0,0) with basic stats and potions.
- Movement is controlled by input keys:
  - `w` = up
  - `s` = down
  - `a` = left
  - `d` = right
- Entering a room triggers events based on room type (combat, item acquisition, or special rooms).
- Combat is turn-based: player can attack, defend, use potions, or attempt to flee.
- Defeating enemies, collecting items, and upgrading stats improve the player's chances.
- The game ends when the player finds the rare sword and escapes, or if the player's HP reaches zero.

## Features

- Procedurally generated 4x4 map with randomized enemy and item placements.
- Turn-based combat system with attack, defense, item usage, and flee mechanics.
- Inventory system with consumable items and equipment upgrades.
- Simple text-based interface that tracks player's position and status.
- Clear victory and game-over conditions.

## Requirements

- Python 3.x

## Future Improvements

- Implement mana system for mana potions.

- Expand map size and room variety.

- Add save/load game functionality.

- Include graphical interface for better user experience.

## How to Run


Run the main script with:

```bash
python3 procedural_rpg.py

Author: " Arthur Mynjko "


