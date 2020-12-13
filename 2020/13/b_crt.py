from math import floor
from operator import itemgetter


with open("input", 'r') as f:
    lines = f.readlines()

bus_line = lines[1].split(',')
buses = [(int(bus_line[i]), i) for i in range(len(bus_line)) if bus_line[i] != 'x']
buses = sorted(buses, key=lambda bus: bus[0], reverse=True)  # sorting to get the greatest modulo first (makes sieving faster)
buses = [(bus[0], bus[1] % bus[0]) for bus in buses]  # making sure a_i < n_i

print(buses)

increment = buses[0][0] 
cong_number = -buses[0][1] % increment
for i, bus in enumerate(buses[1:]):
    while True:
        # find number congruent to a_(i+1) mod n_(i+1)
        if -cong_number % bus[0] == bus[1]:
            break
        cong_number += increment
    increment *= bus[0]  # increment is the product of all "covered" modulos, so for ith step n_1 * n_2 * ... * n_(i-1)

print(cong_number)

