total_fuel = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        mass = int(line)
        mass_fuel_increment = mass // 3 - 2
        total_fuel += mass_fuel_increment

        fuel_fuel_increment = mass_fuel_increment
        while fuel_fuel_increment > 0:
            fuel_fuel_increment = fuel_fuel_increment // 3 - 2
            if fuel_fuel_increment < 0:
                break
            total_fuel += fuel_fuel_increment
            if fuel_fuel_increment < 3 * 3 - 1:
                break

print(total_fuel)
