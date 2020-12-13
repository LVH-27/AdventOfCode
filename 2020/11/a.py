from copy import deepcopy


def adjacent_occupied(row, col, layout):
    edge_left = True if col - 1 < 0 else False
    edge_right = True if col + 1 >= len(layout[0]) else False
    edge_top = True if row - 1 < 0 else False
    edge_bottom = True if row + 1 >= len(layout[0]) else False

    adjacent_y = [n for n in [row - 1, row, row + 1] if n >= 0 and n < len(layout)]
    adjacent_x = [n for n in [col - 1, col, col + 1] if n >= 0 and n < len(layout[0])]

    occupied_count = 0

    for y in adjacent_y:
        for x in adjacent_x:
            if x == col and y == row:
                continue
            if layout[y][x] == '#':
                occupied_count += 1
    return occupied_count


with open("input", "r") as f:
    lines = [list(line.replace('L', '#').strip()) for line in f.readlines()]

adjacent_limit = 4

curr_state = lines
print(lines)
next_state = deepcopy(curr_state)
change_detected = True
pass_number = 0

while change_detected:
    adj = [[0 for i in range(len(line))] for line in lines]
    pass_number += 1
    change_detected = False
    for i in range(len(curr_state)):
        row = curr_state[i]
        for j in range(len(row)):
            # print(pass_number, i, j)
            adjacent_count = adjacent_occupied(row=i, col=j, layout=curr_state)
            adj[i][j] = adjacent_count
            if curr_state[i][j] == '.':
                continue
            if adjacent_count >= adjacent_limit:
                if curr_state[i][j] == '#':
                    change_detected = True
                next_state[i][j] = 'L'
            elif adjacent_count == 0:
                if curr_state[i][j] == 'L':
                    change_detected = True
                next_state[i][j] = '#'

    for row in range(len(curr_state)):
        changed = curr_state[row] == next_state[row]
        print(''.join(curr_state[row]), ' - ', ''.join([str(n) for n in adj[row]]), ' - ', ''.join(next_state[row]), changed)
    # input()
    print()

    curr_state = deepcopy(next_state)
    next_state = deepcopy(curr_state)

print(sum([line.count('#') for line in curr_state]))

