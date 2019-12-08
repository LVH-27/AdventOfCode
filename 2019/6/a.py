with open("input.txt") as f:
    orbit_pairs = [line.strip().split(')') for line in f.readlines()]

direct_orbits = {}

for orbit_pair in orbit_pairs:
    orbiter = orbit_pair[1]
    orbitee = orbit_pair[0]
    direct_orbits[orbiter] = orbitee

orbit_count = 0
indirect_orbits = []
for object in direct_orbits:
    curr_object = object
    next_object = direct_orbits[curr_object]
    while next_object != "COM":
        orbit_count += 1
        print(curr_object, "->", next_object)
        indirect_orbits.append[(object, next_object)]
        curr_object = next_object
        next_object = direct_orbits[curr_object]

print(indirect_orbits)
print(orbit_count)
