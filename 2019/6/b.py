from aocd import submit


def get_common_ancestor(source, target):
    visited = []
    aux_source = source
    aux_target = target
    while True:
        aux_source = direct_orbits[aux_source] if aux_source != "COM" else "COM"
        aux_target = direct_orbits[aux_target] if aux_target != "COM" else "COM"
        if aux_target in visited:
            return aux_target
        if aux_source in visited:
            return aux_source
        visited.append(aux_source)
        visited.append(aux_target)


def get_distance(source, target):
    curr_object = source
    aux_object = direct_orbits[curr_object]
    orbit_transfer_count = 0
    while aux_object != target:
        orbit_transfer_count += 1
        curr_object = aux_object
        aux_object = direct_orbits[curr_object]
    return orbit_transfer_count


with open("input.txt") as f:
    orbit_pairs = [line.strip().split(')') for line in f.readlines()]

direct_orbits = {}

for orbit_pair in orbit_pairs:
    orbiter = orbit_pair[1]
    orbitee = orbit_pair[0]
    direct_orbits[orbiter] = orbitee

orbit_transfer_count = 0

source = "YOU"
target = "SAN"

common_ancestor = get_common_ancestor(source, target)

print(common_ancestor)
result = get_distance(source, common_ancestor) + get_distance(target, common_ancestor)
print(result)

submit(result, part='b', day=6, year=2019)
