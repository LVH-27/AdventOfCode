import re


with open("input", 'r') as f:
    lines = [s.strip() for s in f.readlines()]

mask = lines[0].split(" = ")[1]
regex_mask = re.compile("mask = ([0-1X]+)")
regex_mem = re.compile("mem\[([0-9]+)\] = ([0-9]+)")

memory = {}

for line in lines[1:]:
    if (match := regex_mask.match(line)) is not None:
        mask = match.groups()[0]
    else:
        location, value = [int(n) for n in regex_mem.match(line).groups()]
        value_bin = list(format(value, '036b'))  # pad it to 36 bits
        for i, bit in enumerate(mask):
            if bit == 'X':
                continue
            value_bin[i] = bit
        memory[location] = int(''.join(value_bin), 2)

print(sum(memory.values()))

