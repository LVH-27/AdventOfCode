from aocd import get_data, submit
from os.path import exists

if exists("input.txt"):
    with open("input.txt") as f:
        data = f.readlines()
else:
    data = get_data(day=5, year=2019)
    with open("input.txt", "w") as f:
        data = f.write(data)


result = TODO
submit(result, part='a', day=5, year=2019)
