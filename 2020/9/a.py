from itertools import combinations


with open("input", "r") as f:
    lines = [int(n) for n in f.readlines()]

preamble_length = 25

for i in range(preamble_length, len(lines)):
    found_pair = False
    for pair in combinations(lines[i - preamble_length:i], 2):
        print(pair, lines[i])
        if pair[0] == pair[1] or pair[0] + pair[1] != lines[i]:
            continue
        else:
            found_pair = True
            break
    if not found_pair:
        print(lines[i])
        break

