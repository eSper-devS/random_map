# random_map

A simple Python script for choosing a random map to play.

Used for "Rotation rooms" on S4MAX.

```
$ python3 random_map.py
```

It'll ask you the random style to use:

```
Choose random style:

Mode
Map
>
```

Enter either Mode or Map ("Mode Rotation" uses the Mode version, it is the best tested version). If you type `Mode` and then press `Enter` it will look as such:

```
Choose mode:

TD (["Station-2 (16)", "Steel Cage (16)"])

DM (["Neden-2 (16)", "Neoniac (12)"])

[...]

> [TD]
```

As you can see, "TD" is prefilled. You can simply press `Enter` to get the next TD map in the list (in this case the 16 player map Station-2). If you want to get a map for another mode, just type that mode name follow by `Enter` (in this case, typing `DM` will give you the 16 player map Neden-2).

After pressing `Enter`, the script will output something like:
```
Chosen map: Station-2 (16)
```

If you made a mistake, you can press `Ctrl+D` to kill the script at this point without saving. If you press `Enter`, the selected map will be removed from the queue and the prefill will switch to the next mode in the list. The updated list will be saved to a json file in the same directory.

Useful notes:
- The script will always give you the first map in the list, but sometimes the next map is just not a good fit. You can type `shuffle` to randomize the map order for all modes and update the saved file.)
- When no unplayed maps remain for a mode, the script will put all available maps for that mode back in the queue in a random order.

As you can see, the script is designed so you most of the time only have to press `Enter`. It's not perfect, but it's a good way to make sure each map gets played the same amount of times.
