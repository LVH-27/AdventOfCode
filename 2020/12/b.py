from math import sqrt, atan, sin, cos, radians, degrees, pi


with open("input", 'r') as f:
    lines = f.readlines()


def manhattan(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def rotate_waypoint(way_pos, angle):
    def calc_phi(point):
        if point[0] == 0:
            phi = 90 if point[1] > 0 else 270
        else:
            phi = degrees(atan(point[1] / point[0]))
            if point[0] < 0:
                phi = 180 + phi
        return phi

    print(way_pos)
    calc_r = lambda t: sqrt(t[0] ** 2 + t[1] ** 2) 
    # calc_phi = lambda t: degrees(atan(t[1] / t[0])) if t[0] != 0 else (90 if t[1] > 0 else 270)
    calc_point = lambda r, phi: (round(cos(phi) * r), round(sin(phi) * r))

    r = calc_r(way_pos)
    phi = calc_phi(way_pos)

    new_phi = phi + angle
    print(phi, new_phi, angle)
    new_waypoint = calc_point(r, radians(new_phi))
    print(new_waypoint)
    return new_waypoint 


directions = {
        0: 'E',
        90: 'N',
        180: 'W',
        270: 'S'
    }

actions = {
        'N': lambda distance, cur_pos: (cur_pos[0], cur_pos[1] + distance),
        'S': lambda distance, cur_pos: (cur_pos[0], cur_pos[1] - distance),
        'E': lambda distance, cur_pos: (cur_pos[0] + distance, cur_pos[1]),
        'W': lambda distance, cur_pos: (cur_pos[0] - distance, cur_pos[1]),
        'L': lambda angle, waypoint_pos: rotate_waypoint(waypoint_pos, angle),
        'R': lambda angle, waypoint_pos: rotate_waypoint(waypoint_pos, -angle),
        'F': lambda multiplier, cur_pos, waypoint_pos: (cur_pos[0] + waypoint_pos[0] * multiplier, cur_pos[1] + waypoint_pos[1] * multiplier)
    }


direction = 0
start_pos = (0, 0)
cur_pos = start_pos 

waypoint_start = (10, 1)
waypoint_cur = waypoint_start

for line in lines:
    print(line.strip())
    action = line[0]
    value = int(line[1:])
    
    if action in "NEWS":
        waypoint_cur = actions[action](value, waypoint_cur)
    elif action in "LR":
        waypoint_cur = actions[action](value, waypoint_cur)
    else:
        cur_pos = actions[action](value, cur_pos, waypoint_cur)
    print(cur_pos, waypoint_cur, direction)

print(cur_pos, direction, line)
print(manhattan(start_pos, cur_pos))

