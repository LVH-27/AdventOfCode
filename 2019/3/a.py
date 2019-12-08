with open("input.txt") as f:
    wires = [dir_change.split(',') for dir_change in f.readlines()]

for wire in wires:
    path_points = []
    for dir_change in wire:
        direction = dir_change[0]
        distance = int(dir_change[1:])
        if dir
