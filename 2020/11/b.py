from copy import deepcopy


def visible_occupied(row, col, layout):
    eligible_rows = {
            "left": lambda row, col: [] if col == 0 else layout[row][:col][::-1],  # reverse because we only need the first chair's status
            "right": lambda row, col: [] if col == len(layout[row]) - 1 else layout[row][col + 1:],
            "up": lambda row, col: [] if row  == 0 else [seat[col] for seat in layout[:row]][::-1],
            "down": lambda row, col: [] if row == len(layout) - 1 else [seat[col] for seat in layout[row + 1:]],
            "diag_up_left": lambda row, col: [] if row == 0 or col == 0 else [layout[row - off][col - off] for off in range(1, 1 + min(len(layout[:row]), len(layout[row][:col])))],
            "diag_up_right": lambda row, col: [] if row == 0 or col == len(layout[row]) - 1 else [layout[row - off][col + off] for off in range(1, 1 + min(len(layout[:row]), len(layout[row][col + 1:])))],
            "diag_down_left": lambda row, col: [] if row == len(layout) - 1 or col == 0 else [layout[row + off][col - off] for off in range(1, 1 + min(len(layout[row + 1:]), len(layout[row][:col])))],
            "diag_down_right": lambda row, col: [] if row == len(layout) - 1 or col == len(layout[row]) - 1 else [layout[row + off][col + off] for off in range(1, 1 + min(len(layout[row + 1:]), len(layout[row][col + 1:])))]
    }

    visible_count = 0

    for direction in eligible_rows:
        eligible = eligible_rows[direction](row, col)
        # print(row, col, direction, eligible)
        for spot in eligible:
            if spot == '.':
                continue
            if spot == '#':
                # print("\tFound visible:", spot)
                visible_count += 1
                break
            if spot == 'L':
                break
    # print("Visible count:", visible_count)
    return visible_count


with open("input", "r") as f:
    lines = [list(line.replace('L', '#').strip()) for line in f.readlines()]

visible_limit = 5

curr_state = lines
for row in lines:
    print(''.join(row))
next_state = deepcopy(curr_state)
change_detected = True
pass_number = 0

while change_detected:
    visible = [[0 for i in range(len(line))] for line in lines]
    pass_number += 1
    change_detected = False
    for i in range(len(curr_state)):
        row = curr_state[i]
        for j in range(len(row)):
            # print(pass_number, i, j)
            visible_count = visible_occupied(row=i, col=j, layout=curr_state)
            visible[i][j] = visible_count
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
    #     print(''.join(curr_state[row]), ' - ', ''.join([str(n) for n in visible[row]]), ' - ', ''.join(next_state[row]), changed)
    # # input()

    curr_state = deepcopy(next_state)
    next_state = deepcopy(curr_state)

print(sum([line.count('#') for line in curr_state]))

