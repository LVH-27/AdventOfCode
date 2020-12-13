with open("input", "r") as f:
    lines = [int(n) for n in f.readlines()]


last_joltage = 0
allowed_range = [1, 2, 3]

adapters_sorted = sorted(lines)[::-1]  # reversing them for popping
print(adapters_sorted)

diffs = {1: [], 2: [], 3: []}
device_joltage = max(adapters_sorted) + 3

while last_joltage < device_joltage - 3:
    adapter = adapters_sorted.pop()
    diff = adapter - last_joltage
    print(last_joltage, adapter, diff)
    if diff > 0 and diff <= 3:
        diffs[diff].append(adapter)
    else:
        raise IndexError
    last_joltage = adapter

diffs[3].append(device_joltage)
print(len(diffs[1]) * len(diffs[3]))

