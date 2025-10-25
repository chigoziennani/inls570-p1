"""Checkpoint 1 + Final for Project 1 - Simple Text Adventure Game"""

# function that loads game data from configuration file
def load_game(filename):
    gameinfo = {}
    game_map = {}
    npcs = {}

    with open(filename, "r") as f:
        current_room = None
        for line in f:
            line = line.strip()
            if not line or line == "---":
                continue

            parts = line.split(":", 1)
            if len(parts) != 2:
                continue
            key, value = parts
            key = key.strip()
            value = value.strip()

            if key.startswith("game_"):
                gameinfo[key] = value
            elif key == "r_id":
                current_room = value
                if current_room not in game_map:
                    game_map[current_room] = {"id": current_room, "obj": []}
            elif key == "r_obj":
                if current_room:
                    game_map[current_room]["obj"].append(value)
            elif key.startswith("r_"):
                if current_room:
                    game_map[current_room][key[2:]] = value
            elif key.startswith("npc_"):
                npc_parts = key.split("_")
                npc_name = npc_parts[1]
                npc_prop = npc_parts[2]
                if npc_name not in npcs:
                    npcs[npc_name] = {}
                npcs[npc_name][npc_prop] = value

    return gameinfo, game_map, npcs


# function that handles player movement
def move_player(current, direction, gameinfo, game_map):
    xsize, ysize = int(gameinfo["game_xsize"]), int(gameinfo["game_ysize"])
    cur = int(current)

    # calculates current row and column
    row = (cur - 1) // xsize
    col = (cur - 1) % xsize

    # updates row and column based on direction with wrap-around
    if direction == "north":
        row = (row - 1) % ysize
    elif direction == "south":
        row = (row + 1) % ysize
    elif direction == "west":
        col = (col - 1) % xsize
    elif direction == "east":
        col = (col + 1) % xsize

    # calculates new location ID
    new_loc = row * xsize + col + 1
    new_loc = str(new_loc)

    # checks for movement overrides
    if direction in game_map[current]:
        new_loc = game_map[current][direction]

    return new_loc


# main game function
def main():
    # Load game data
    filename = input("Enter config file (e.g., game1.txt): ")
    gameinfo, game_map, npcs = load_game(filename)

    # welcome message and game goal
    print(f"Welcome to {gameinfo['game_name']}\n")
    print(f"The goal of this game is to:\n{gameinfo['game_goal']}\n")

    # initializes player state
    current = gameinfo["game_start"]
    inventory = []

    # main game loop
    while True:
        # checks for win condition
        goal_loc = gameinfo.get("game_goalloc")
        goal_obj = gameinfo.get("game_goalobj")
        if goal_loc and goal_obj and goal_loc in game_map and goal_obj in game_map[goal_loc].get(
            "obj", []
        ):
            print("Congratulations! You have won the game.")
            break

        # displays current room description and objects
        room = game_map[current]
        print(f"You are {room['desc']}")

        if room.get("obj"):
            for item in room["obj"]:
                print(f"There is a {item} here.")

        # gets and processes user command
        command = input("What next? ").strip().lower()
        print()
        if not command:
            continue

        parts = command.split()
        verb = parts[0]

        if command == "exit":
            break
        elif verb == "move":
            if len(parts) == 2:
                direction = parts[1]
                if direction == "path":
                    # handles hidden path movement
                    if "found_path" in room and room["found_path"]:
                        current = room["hiddenpath"]
                    else:
                        print("You haven't found a hidden path here.")
                else:
                    current = move_player(current, direction, gameinfo, game_map)
            else:
                print("Move where? north/south/east/west")
        elif command == "inv":
            print(f"Your inventory: {inventory}")
        elif command == "goal":
            print(f"The goal of this game is to:\n{gameinfo['game_goal']}\n")
        elif verb == "take":
            if len(parts) == 2:
                obj_to_take = parts[1]
                if obj_to_take in room.get("obj", []):
                    room["obj"].remove(obj_to_take)
                    inventory.append(obj_to_take)
                else:
                    print("That object is not here.")
            else:
                print("Take what?")
        elif verb == "drop":
            if len(parts) == 2:
                obj_to_drop = parts[1]
                if obj_to_drop in inventory:
                    inventory.remove(obj_to_drop)
                    room["obj"].append(obj_to_drop)
                else:
                    print("You are not carrying that object.")
            else:
                print("Drop what?")
        elif command == "search":
            found_something = False
            # searches for hidden objects
            if "hiddenobj" in room:
                hidden = room.pop("hiddenobj")
                room["obj"].append(hidden)
                print(f"You found a {hidden}")
                found_something = True
            # searches for hidden paths
            if "hiddenpath" in room:
                room["found_path"] = True
                print("You found a hidden path!")
                found_something = True

            if not found_something:
                print("You find nothing special.")
        elif verb == "talk":
            if len(parts) > 1:
                npc_name = parts[1].capitalize()
                npc_found = False
                for npc, data in npcs.items():
                    if npc.lower() == npc_name.lower() and data["loc"] == current:
                        npc_found = True
                        # provides different dialogue on first and subsequent talks
                        if "talked" not in data:
                            print(data["1"])
                            data["talked"] = True
                        else:
                            print(data["2"])
                        break
                if not npc_found:
                    print("That person is not here.")
            else:
                print("Talk to whom?")
        else:
            print("Unknown command (try 'move north' or 'exit').")


# runs the main function when the script is executed
if __name__ == "__main__":
    main()