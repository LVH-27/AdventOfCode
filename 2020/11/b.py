from copy import deepcopy


def visible_occupied(row, col, layout):
    visible_y = []
    visible_x = []

    occupied_count = 0

    for y in visible_y:
        for x in visible_x:
            if x == col and y == row:
                continue
            if layout[y][x] == '#':
                occupied_count += 1
    return occupied_count


with open("input", "r") as f:
    lines = [list(line.replace('L', '#').strip()) for line in f.readlines()]

visible_limit = 4

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
            visible_count = visible_occupied(row=i, col=j, layout=curr_state)
            adj[i][j] = visible_count
            if curr_state[i][j] == '.':
                continue
            if visible_count >= visible_limit:
                if curr_state[i][j] == '#':
                    change_detected = True
                next_state[i][j] = 'L'
            elif visible_count == 0:
                if curr_state[i][j] == 'L':
                    change_detected = True
                next_state[i][j] = '#'

    # for row in range(len(curr_state)):
    #     changed = curr_state[row] == next_state[row]
    #     print(''.join(curr_state[row]), ' - ', ''.join([str(n) for n in adj[row]]), ' - ', ''.join(next_state[row]), changed)
    # input()

    curr_state = deepcopy(next_state)
    next_state = deepcopy(curr_state)

print(sum([line.count('#') for line in curr_state]))

