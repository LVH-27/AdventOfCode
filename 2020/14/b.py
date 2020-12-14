import re


def get_all_combinations(possible_locations, bit_x):
    """docstring for get_all_combinations"""
    aux_locations = []
    for location_bin in possible_locations:
        location_bin_0 = list(location_bin)
        location_bin_0[bit_x] = '0'
        location_bin_1 = list(location_bin)
        location_bin_1[bit_x] = '1' 

        if location_bin_0 not in possible_locations:
            aux_locations.append(location_bin_0)
        if location_bin_1 not in possible_locations:
            aux_locations.append(location_bin_1)
    return aux_locations


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
        location_bin = list(format(location, '036b'))
        possible_locations = [location_bin]
        for i, bit in enumerate(mask):
            if bit == 'X':
                possible_locations.extend(get_all_combinations(possible_locations, i))
            elif bit == '1':
                possible_locations = [loc[:i] + ['1'] + loc[i + 1:] for loc in possible_locations]  # set ones wherever necessary

        for loc_bin in possible_locations:
            print(loc_bin)
            loc = int(''.join(loc_bin), 2)
            memory[loc] = value

print(sum(memory.values()))

