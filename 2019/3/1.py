
def change_direction(new_direction):
    global curr_direction
    if new_direction == 'R':
        curr_direction = (curr_direction + 1) % 4
    else:
        curr_direction = (curr_direction - 1) % 4


def move(movement):
    global curr_direction
    global hor_dist
    global ver_dist
    global first
    new_direction, diiistance = movement[0], int(movement[1:])
    change_direction(new_direction)

    for distance in range(1, diiistance + 1):
        if curr_direction == 0:
            ver_dist += 1
        elif curr_direction == 1:
            hor_dist += 1
        elif curr_direction == 2:
            ver_dist -= 1
        elif curr_direction == 3:
            hor_dist -= 1

        if (hor_dist, ver_dist) not in visited:
            visited[(hor_dist, ver_dist)] = 1
        elif not first:
            visited[(hor_dist, ver_dist)] += 1
            first = True


def get_distance_from_start(hor_dist, ver_dist):
    return abs(hor_dist) + abs(ver_dist)


hor_dist = 0
ver_dist = 0
currDirection = 0
first = False

visited = {}
visited[(0, 0)] = 1

with open("input.txt") as f:
    wires = [dir_change.split(',') for dir_change in f.readlines()]

for wire in wires:
    for movement in wire:
        move(movement)
        print(movement, currDirection, hor_dist, ver_dist, get_distance_from_start(hor_dist, ver_dist))

for tup in visited:
    if visited[tup] != 1:
        print(get_distance_from_start(tup[0], tup[1]))
