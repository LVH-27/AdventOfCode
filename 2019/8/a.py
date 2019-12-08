from aocd import get_data, submit
from collections import defaultdict
from os.path import exists


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

digit_counts = []
min_zero_count = None
min_zero_index = None
for layer_index in range(len(image_data)):
    layer = image_data[layer_index]
    digit_count = defaultdict(int)
    for row_index in range(len(layer)):
        digit_count[0] += layer[row_index].count(0)
        digit_count[1] += layer[row_index].count(1)
        digit_count[2] += layer[row_index].count(2)
        print(row_index, layer[row_index], digit_count[0], digit_count[1], digit_count[2])

    if min_zero_count is None:
        min_zero_count = digit_count[0]
        min_zero_index = layer_index
    else:
        min_zero_index = layer_index if min_zero_count > digit_count[0] else min_zero_index
        min_zero_count = digit_count[0] if min_zero_count > digit_count[0] else min_zero_count
    print(digit_count)
    print(min_zero_index, min_zero_count)
    # input()
    digit_counts.append(digit_count)
    print()

min_layer = image_data[min_zero_index]
result = digit_counts[min_zero_index][1] * digit_counts[min_zero_index][2]
print(result)
print(image_data[min_zero_index])
print(digit_counts[min_zero_index][0])
print(digit_counts[min_zero_index][1])
print(digit_counts[min_zero_index][2])
# submit(result, part='a', day=day, year=2019)
