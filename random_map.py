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
        "Steelcage",
        "Galleon EX",
        "Bladecity",
        "Ironheart",
        "Neden-1",
        "City Square",
        "Station-2 (Minecraft)",
        "MAX School",
        "Tunnel-Pro",
        "Cyberion",
        "Sector-R",
        "Temple-R",
        "Ziggurat",
        "Neo-Wonder",
        "Station-3",
        "IS-06",
        "Hyperium",
        "Side-3",
        "Tunnel",
        "Neden-3",
        "Station-2",
        "Station-1",
        "Highway",
        "Old School",
        "Temple-M",
        "Colosseum"
    ],
    "Siege": [
        "Sector-R",
        "Bladecity",
        "Skyline",
        "Ironheart"
    ],
    "DM": [
        "Data Harvest",
        "The Longest Yard",
        "Cyberion",
        "Xenotron Cluster",
        "OldMoon",
        "City Square-2",
        "Ziggurat",
        "Alpha Circle",
        "Dust 2",
        "Mansion",
        "Neden-1 S",
        "Mansion Grounds",
        "Warp-Ship",
        "Bio-Lab",
        "Spade A",
        "Construction",
        "Neden-J",
        "Azit",
        "Azit-EX",
        "Square",
        "HoliDay",
        "Neoniac",
        "Luna-2",
        "Treasure",
        "Neden-1",
        "Galleon",
        "Neden-2",
        "Neden-3",
        "Highway",
        "Circle-1",
        "BlockBuster"
    ],
    "Chaser": [
        "Alice House",
        "The Longest Yard",
        "Galleon EX",
        "Xenotron Cluster",
        "Grave",
        "Nightmare",
        "Temple-O",
        "Connest-2",
        "Circle-2",
        "BlockBuster",
        "Office"
    ],
    "BR": [
        "Data Harvest",
        "The Longest Yard",
        "Xenotron Cluster",
        "City Square-2",
        "Ziggurat",
        "MAX School",
        "Alpha Circle",
        "Neoniac",
        "Galleon",
        "Dust 2"
    ],
    "Captain": [
        "The Longest Yard",
        "Spade A",
        "Azit-EX",
        "Nightmare",
        "OldMoon"
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
