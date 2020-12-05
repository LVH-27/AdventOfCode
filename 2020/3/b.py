with open("input", "r") as f:
    lines = f.readlines()

patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_tree_count = 1
line_length = len(lines[0]) - 1

for pattern in patterns:
    print(pattern)
    tree_count = 0
    i = 0
    x_pos = 0 
    while i < len(lines):
#        print(i, x_pos, tree_count)
        if lines[i][x_pos] == "#":
            tree_count += 1
        x_pos = (x_pos + pattern[0]) % line_length
        i += pattern[1]
    print(tree_count)
    input()
    total_tree_count *= tree_count
print(total_tree_count)

