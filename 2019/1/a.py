total_fuel = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        mass = int(line)
        total_fuel += int(mass / 3) - 2

print(total_fuel)
