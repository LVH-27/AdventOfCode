#!/usr/bin/python3


frequencies = [0]
with open('in.txt', 'r') as f:
    lines = f.read().split()

frequency = frequencies[0]
found = False
while not found:
    for line in lines:
        if line[0] == '+':
            frequency += int(line[1:])
        else:
            frequency -= int(line[1:])
        if frequency in frequencies:
            found = True
            break
        else:
            frequencies.append(frequency)

print(frequency)
