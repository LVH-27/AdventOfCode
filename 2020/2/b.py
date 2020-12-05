with open("input", "r") as f:
    lines = f.readlines()

valid_count = 0
for line in lines:
    line_split = line.split(' ')
    policy_range = [int(n) for n in line_split[0].split('-')]
    policy_char = line_split[1][0]
    password = line_split[-1].strip()

    print(policy_range, policy_char, password)

    first_has_char = password[policy_range[0] - 1] == policy_char
    second_has_char = password[policy_range[1] - 1] == policy_char
    if first_has_char != second_has_char:
        print("inc")
        valid_count += 1
    print()

print(valid_count)

