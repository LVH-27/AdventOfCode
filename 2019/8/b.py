from aocd import get_data, submit
from os.path import exists
from pprint import pprint


day = 8

if exists("input.txt"):
    with open("input.txt") as f:
        data = f.read()
else:
    data = get_data(day=day, year=2019)
    with open("input.txt", "w") as f:
        data = f.write(data)


image_dim = (25, 6)
image_data = []
data = [int(digit) for digit in data][::-1]  # reverse for popping

while len(data) > 0:
    current_layer = []
    while len(current_layer) < image_dim[1]:
        current_layer.append([])
        while len(current_layer[-1]) < image_dim[0]:
            current_layer[-1].append(data.pop())
    image_data.append(current_layer)

final_image = [[2 for pixel in range(image_dim[0])] for row in range(image_dim[1])]

for y in range(image_dim[1]):
    for x in range(image_dim[0]):
        if final_image[y][x] != 2:
            continue
        for layer_index in range(len(image_data)):
            layer_value = image_data[layer_index][y][x]
            if layer_value == 0 or layer_value == 1:
                final_image[y][x] = layer_value
                break

final_image = [''.join([str(digit) for digit in row]) for row in final_image]
pprint(final_image)
# submit(result, part='b', day=day, year=2019)
