from aocd import get_data, submit


def double_not_part_of_larger_group(candidate):
    str_candidate = str(candidate)
    for i in range(1, len(str_candidate)):
        if str_candidate[i] == str_candidate[i - 1]:
            if str_candidate.count(str_candidate[i]) == 2:
                return True
    return False


def double_found(candidate):
    str_candidate = str(candidate)
    for i in range(1, len(str_candidate)):
        if str_candidate[i] == str_candidate[i - 1]:
            return True
    return False


def nondecreasing(candidate):
    str_candidate = str(candidate)
    for i in range(1, len(str_candidate)):
        if int(str_candidate[i]) < int(str_candidate[i - 1]):
            return False
    return True


with open("input.txt") as f:
    line = f.read()
    password_range = [int(n) for n in line.split('-')]

valid_passwords = []
for pass_candidate in range(password_range[0], password_range[1]):
    if double_found(pass_candidate) and nondecreasing(pass_candidate):
        if double_not_part_of_larger_group(pass_candidate):
            valid_passwords.append(pass_candidate)

print(len(valid_passwords))
# submit(len(valid_passwords), part='a', day='4', year='2019')
