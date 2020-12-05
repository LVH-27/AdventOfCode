with open("input", "r") as f:
    lines = f.readlines()

valid_count = 0
for line in lines:
    line_split = line.split(' ')
    policy_range = [int(n) for n in line_split[0].split('-')]
    policy_char = line_split[1][0]
    password = line_split[-1].strip()

    print(policy_range, policy_char, password)

    pw_char_count = password.count(policy_char)
    print("pw cnt", pw_char_count)
    if pw_char_count >= policy_range[0] and pw_char_count <= policy_range[1]:
        print("inc")
        valid_count += 1
    print()

print(valid_count)

