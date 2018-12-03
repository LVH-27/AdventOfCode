#!/usr/bin/python3
from collections import Counter


with open('in.txt', 'r') as f:
    lines = f.read().split()

counter = {
    2: 0,
    3: 0
}

for line in lines:
    found_letters = Counter()
    for char in line:
        found_letters[char] += 1

    for letter in found_letters:
        if found_letters[letter] == 2:
            counter[2] += 1
            break

    for letter in found_letters:
        if found_letters[letter] == 3:
            counter[3] += 1

print("{} * {} = {}".format(counter[2], counter[3], counter[2] * counter[3]))
