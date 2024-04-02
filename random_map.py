#!/bin/python3

import json
import random
from os import system


def save(maps, style):
    with open('random_map_' + style + '.json', 'w') as f:
        f.write(json.dumps(maps))


def load(style):
    try:
        with open('random_map_' + style + '.json', 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        print("Could not load random_map.json")


def random_style_mode():
    map_data = load('mode')
    if map_data:
        maps = map_data
    else:
        maps = {}
        for mode in all_maps:
            maps[mode] = random.sample(all_maps[mode], len(all_maps[mode]))

    index = 0
    index_mode = None

    while True:
        save(maps, 'mode')
        if index >= len(maps):
            index = 0

        system('clear')
        print("Choose mode:\n")
        for mode_index, mode in enumerate(maps):
            if index == mode_index:
                index_mode = mode
            print(f"{mode} ({maps[mode]})")
            print()

        chosen_mode = input(f"> [{index_mode}] ")
        if not chosen_mode:
            chosen_mode = index_mode

        if chosen_mode == "shuffle":
            for mode in maps:
                maps[mode] = random.sample(maps[mode], len(maps[mode]))
        elif chosen_mode in maps:
            chosen_map = maps[chosen_mode].pop(0)
            print(f"Chosen map: {chosen_map}")

            for mode in maps:
                if len(maps[mode]) == 0:
                    print(f"Queue for {mode} is empty, refilling it...")
                    maps[mode] = random.sample(all_maps[mode], len(all_maps[mode]))

            input()

            for mode_index, mode in enumerate(maps):
                if mode == chosen_mode:
                    index = mode_index + 1


def random_style_map():
    map_data = load('map')
    if map_data:
        maps = map_data
    else:
        maps = []
        for mode in all_maps:
            for _map in all_maps[mode]:
                if _map not in maps:
                    maps.append(_map)

    maps = random.sample(maps, len(maps))

    while True:
        save(maps, 'map')
        chosen_map = maps.pop(0)
        supported_modes = []
        for mode in all_maps:
            if chosen_map in all_maps[mode]:
                supported_modes.append(mode)
        chosen_mode = random.choice(supported_modes)

        print(f"Chosen: {chosen_map} ({chosen_mode})")

        input()


random_styles = {
    "Mode": random_style_mode,
    "Map": random_style_map
}
all_maps = {
    "TD":
    [
        "PlayField (16)",
        "SteelCage (16)",
        "Galleon EX (16)",
        "Bladecity (16)",
        "Ironheart (16)",
        "Neden-1 (16)",
        "City Square (16)",
        "Station-2 [Minecraft] (16)",
        "Max School (16)",
        "Tunnel-Pro (16)",
        "Cyberion (16)",
        "Sector-R (16)",
        "Temple-R (16)",
        "Ziggurat (16)",
        "Neo-Wonder (16)",
        "Station-3 (16)",
        "IS-06 (16)",
        "Hyperium (16)",
        "Side-3 (16)",
        "Tunnel (16)",
        "Neden-3 (16)",
        "Station-2 (16)",
        "Station-1 (16)",
        "Highway (16)",
        "Old School (16)",
        "Temple-M (16)",
        "Colosseum (16)"
    ],
    "DM": [
        "Bamboo Forest (12)",
        "Cylot (10)",
        "Beach (12)",
        "Stadium City (16)",
        "Airship Cafe (8)",
        "Neden-2 W (16)",
        "Azit-O (8)",
        "Data Harvest (16)",
        "The Longest Yard (16)",
        "Cyberion (16)",
        "Xenotron Cluster (16)",
        "OldMoon (16)",
        "City Square-2 (16)",
        "Ziggurat (16)",
        "Alpha Circle (16)",
        "Dust 2 (16)",
        "Mansion (16)",
        "Neden-1 S (16)",
        "Mansion Grounds (16)",
        "Warp-Ship (16)",
        "Bio-Lab (16)",
        "Spade A (16)",
        "Construction (16)",
        "Neden-J (12)",
        "Azit (8)",
        "Azit-EX (16)",
        "Square (16)",
        "HoliDay (12)",
        "Neoniac (12)",
        "Luna-2 (12)",
        "Treasure (12)",
        "Galleon (16)",
        "BlockBuster (12)",
        "Circle-1 (12)",
        "Highway (16)",
        "Neden-3 (12)",
        "Neden-2 (12)",
        "Neden-1 (12)"
    ],
    "Chaser": [
        "Bamboo Forest (12)",
        "Airship Cafe (10)",
        "Cylot (12)",
        "OldMoon (16)",
        "Mansion Grounds (16)",
        "The Longest Yard (16)",
        "Galleon EX (16)",
        "Xenotron Cluster (16)",
        "Alice House (12)",
        "Grave (12)",
        "Nightmare (12)",
        "Temple-O (12)",
        "Connest-2 (12)",
        "Circle-2 (12)",
        "BlockBuster (12)",
        "Office (12)"
    ],
    "BR": [
        "Temple-R (16)",
        "Stadium City (16)",
        "Beach (12)",
        "Lost Salvage (16)",
        "OldMoon (16)",
        "Mansion Grounds (16)",
        "Data Harvest (16)",
        "The Longest Yard (16)",
        "Xenotron Cluster (16)",
        "City Square-2 (16)",
        "Ziggurat (16)",
        "Max School (16)",
        "Dust 2 (16)",
        "Alpha Circle (16)",
        "Neoniac (16)",
        "Galleon (16)"
    ],
    "Captain": [
        "The Longest Yard (16)",
        "Spade A (16)",
        "Azit-EX (16)",
        "Luna-2 (16)",
        "Nightmare (16)",
        "OldMoon (16)",
        "Neden-1 (16)"
    ],
    "Siege": [
        "Terminal-109 (16)",
        "Lost Salvage (16)",
        "Sector-R (16)",
        "Bladecity (16)",
        "Skyline (16)",
        "Ironheart (16)"
    ]
}

system('clear')
print("Choose random style:\n")

for style in random_styles:
    print(style)

while True:
    random_style = input("> ")
    if random_style in random_styles:
        break

random_styles[random_style]()
