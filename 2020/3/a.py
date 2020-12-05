with open("input", "r") as f:
    lines = f.readlines()

pattern = (3, 1)
tree_count = 0
x_pos = 0 
line_length = len(lines[0]) - 1

i = 0

while i < len(lines):
#    print(i, x_pos, tree_count)
    if lines[i][x_pos] == "#":
        tree_count += 1
    x_pos = (x_pos + pattern[0]) % line_length
    i += pattern[1]
#    print(tree_count)
#    input()
print(tree_count)

