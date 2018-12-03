#!/usr/bin/python3
import re

with open('in.txt', 'r') as f:
    lines = f.read().split('\n')

claims = {}
max_right = 0
max_down = 0
for line in lines:
    claim_id, left_offset, top_offset, width, height =\
        re.match("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", line).groups()
    left_offset = int(left_offset)
    top_offset = int(top_offset)
    width = int(width)
    height = int(height)
    claims[claim_id] = [left_offset, top_offset, width, height]
    if left_offset + width > max_right:
        max_right = left_offset + width
    if top_offset + height > max_down:
        max_down = top_offset + height

fabric = [[0 for i in range(max_right)] for j in range(max_down)]

for claim in claims:
    left_offset, top_offset, width, height = claims[claim]
    for row in range(top_offset, top_offset + height):
        for col in range(left_offset, left_offset + width):
            fabric[row][col] += 1

overlapping_inches = 0

for row in fabric:
    for col in row:
        if col > 1:
            overlapping_inches += 1

print(overlapping_inches)
