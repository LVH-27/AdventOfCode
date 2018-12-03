#!/usr/bin/python3
from Levenshtein import distance


with open('in.txt', 'r') as f:
    lines = f.read().split()

common_lines = None
for i in range(len(lines)):
    for j in range(len(lines)):
        if distance(lines[i], lines[j]) == 1:
            print(lines[i], lines[j])
            common_lines = (lines[i], lines[j])
            break

for c in range(len(common_lines[0])):
    if common_lines[0][c] != common_lines[1][c]:
        print(common_lines[0][:c] + common_lines[0][c+1:])
        break
