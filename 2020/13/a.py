from math import floor


with open("input", 'r') as f:
    lines = f.readlines()

earliest = int(lines[0])
bus_ids = [int(bus_id) for bus_id in lines[1].split(',') if bus_id != 'x']

print(bus_ids)

smallest_wait_time = max(bus_ids) - 1  # initialized to longest possible wait time - 
soonest_bus = -1

for bus in bus_ids:
    drive_count = floor(earliest / bus)
    wait_time = (drive_count + 1) * bus - earliest
    if wait_time < smallest_wait_time:
        smallest_wait_time = wait_time
        soonest_bus = bus

print(soonest_bus, smallest_wait_time, soonest_bus * smallest_wait_time)
