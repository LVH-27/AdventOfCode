with open("input", "r") as f:
    lines = f.readlines()

ROW_ONE = 'B'
ROW_ZERO = 'F'

COL_ONE = 'R'
COL_ZERO = 'L'

ROW_WIDTH = 8


def convert_to_number(string, char_one, char_zero):
    binary = string.replace(char_one, '1').replace(char_zero, '0')
    print(binary)
    return int(binary, 2)     


def get_seat_id(seat_row, seat_col, row_width):
    return seat_row * row_width + seat_col


max_seat = 0
seats = []

for line in lines:
    row_string = line[:-4]
    col_string = line[-4:]
    row = convert_to_number(row_string, ROW_ONE, ROW_ZERO)
    col = convert_to_number(col_string, COL_ONE, COL_ZERO)
    seat_id = get_seat_id(row, col, ROW_WIDTH)

    print(row, col, seat_id)
    if max_seat < seat_id:
        max_seat = seat_id
    seats.append(seat_id)

print(max_seat)

