# INLS570 Project 1 - Text Adventure Game

A simple text-based adventure game implemented in Python for INLS570 (Information Science course).

## Project Overview

This project implements a text adventure game engine that can load game configurations from text files and provide an interactive gaming experience. The game supports:

- Player movement in a grid-based world
- Object collection and inventory management
- NPC interactions with dialogue
- Hidden objects and paths
- Win conditions based on location and object requirements

## Files

- `cfnnani_p1.py` - Main game engine implementation
- `game1.txt` - First adventure scenario
- `game2.txt` - Second adventure scenario
- `inls570-p1-f25.pdf` - Project assignment document

## Game Features

### Commands
- `move [direction]` - Move in a direction (north, south, east, west)
- `move path` - Use a hidden path (if found)
- `take [object]` - Pick up an object
- `drop [object]` - Drop an object from inventory
- `inv` - Display current inventory
- `search` - Search for hidden objects or paths
- `talk [npc]` - Interact with NPCs
- `goal` - Display the game objective
- `exit` - Quit the game

### Game Mechanics
- **Grid Movement**: Players move on a configurable grid with wrap-around
- **Object System**: Objects can be picked up, dropped, and used for win conditions
- **Hidden Elements**: Search command reveals hidden objects and paths
- **NPC Dialogue**: Characters provide different dialogue on first and subsequent interactions
- **Win Conditions**: Complete objectives by bringing specific objects to specific locations

## How to Run

1. Make sure you have Python 3.x installed
2. Run the game:
   ```bash
   python cfnnani_p1.py
   ```
3. When prompted, enter a game configuration file (e.g., `game1.txt` or `game2.txt`)

## Game Scenarios

### Adventure 1
- **Goal**: Find the magic helmet and bring it to Hans
- **Starting Location**: Room 4 (on a path)
- **Special Features**: Hidden helmet in room 5, secret path to Hans

### Adventure 2
- **Goal**: Find the vinegarbbq and bring it to TimmyTarHeel
- **Starting Location**: Room 5 (New Orleans)
- **Special Features**: Multiple NPCs with unique dialogue, city-based locations

## Configuration File Format

Game configurations use a simple text format with the following structure:

```
game_name: [Game Title]
game_goal: [Objective description]
game_goalloc: [Win location ID]
game_goalobj: [Required object]
game_start: [Starting location ID]
game_xsize: [Grid width]
game_ysize: [Grid height]
---
r_id: [Room ID]
r_desc: [Room description]
r_obj: [Object in room]
r_[direction]: [Connected room ID]
r_hiddenobj: [Hidden object]
r_hiddenpath: [Hidden path destination]
---
npc_[name]_loc: [NPC location]
npc_[name]_1: [First dialogue]
npc_[name]_2: [Subsequent dialogue]
```

## Technical Implementation

The game engine consists of several key functions:

- `load_game()` - Parses configuration files and builds game state
- `move_player()` - Handles player movement with grid calculations
- `main()` - Main game loop with command processing

## Author

**Chigozie Nnani** - INLS570 Student

## Course Information

- **Course**: INLS570 - Information Science
- **Project**: Project 1 - Text Adventure Game
- **Semester**: Fall 2025

## License

This project is created for educational purposes as part of INLS570 coursework.
