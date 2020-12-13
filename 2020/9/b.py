from itertools import combinations


with open("input", "r") as f:
    lines = [int(n) for n in f.readlines()]

preamble_length = 25
target_number = 0

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
        target_number = lines[i]
        break


running_total = 0
factor_indices = []
i = 0

while i < len(lines):
    running_total += lines[i]
    factor_indices.append(i)
    if running_total == target_number:
        break
    if running_total > target_number:
        i = factor_indices[1]  # return to the second index of the current numbers window and start a new one
        running_total = 0
        factor_indices = []

    else:
        i += 1

factors = [lines[i] for i in factor_indices]
print(min(factors) + max(factors))

