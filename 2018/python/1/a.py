#!/usr/bin/python3


frequency = 0
with open('in.txt', 'r') as f:
    lines = f.read().split()

for line in lines:
    if line[0] == '+':
        frequency += int(line[1:])
    else:
        frequency -= int(line[1:])

print(frequency)

