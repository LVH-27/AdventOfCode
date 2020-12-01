from itertools import combinations
from math import prod

with open("input", "r") as f:
    numbers = [int(line) for line in f.readlines()]

tuplet_number = 3
for tuplet in combinations(numbers, tuplet_number):
    if sum(tuplet) == 2020:
        print(prod(tuplet))

