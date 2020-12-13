with open("input", 'r') as f:
    lines = f.readlines()


def manhattan(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


directions = {
        0: 'E',
        90: 'N',
        180: 'W',
        270: 'S'
    }

actions = {
        'N': lambda distance, cur_pos: (cur_pos[0], cur_pos[1] + distance),
        'S': lambda distance, cur_pos: (cur_pos[0], cur_pos[1] - distance),
        'E': lambda distance, cur_pos: (cur_pos[0] + distance, cur_pos[1]),
        'W': lambda distance, cur_pos: (cur_pos[0] - distance, cur_pos[1]),
        'L': lambda degrees, direction: (direction + degrees) % 360,
        'R': lambda degrees, direction: (direction - degrees) % 360,
        'F': lambda distance, direction, cur_pos: actions[directions[direction]](distance, cur_pos)
    }


direction = 0
start_pos = (0, 0)
cur_pos = (0, 0)

for line in lines:
    print(line)
    action = line[0]
    value = int(line[1:])
    
    if action in "NEWS":
        cur_pos = actions[action](value, cur_pos)
    elif action in "LR":
        direction = actions[action](value, direction)
    else:
        cur_pos = actions[action](value, direction, cur_pos)
    print(cur_pos, direction)
    #input()

print(cur_pos, direction, line)
print(manhattan(start_pos, cur_pos))

