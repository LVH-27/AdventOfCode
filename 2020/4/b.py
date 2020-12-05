import re


def is_valid(passport, required_fields, validators):
    print(passport)
    for field in required_fields:
        print(field)
        if field not in passport:
            return False
        if not validators[field](passport[field]):
            print(validators[field](passport[field]))
            return False
    return True
 
validators = {
    "byr": lambda year : int(year) >= 1920 and int(year) <= 2002,
    "iyr": lambda year : int(year) >= 2010 and int(year) <= 2020,
    "eyr": lambda year : int(year) >= 2020 and int(year) <= 2030,
    "hgt": lambda hgt : (hgt[-2:] == "cm" and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193) or (hgt[-2:] == "in" and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76),
    "hcl": lambda color : re.match("^#[0-9a-f]{6}$", color),
    "ecl": lambda color : color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda pid : re.match("^[0-9]{9}$", pid),
    "cid": lambda cid : True
}


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

valid_count = 0
valid_passports = []
passports_without_cid = []

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_field = "cid"

reading_pass = False
for line in lines:
    # print(line)
    if len(line) == 0:
        valid = is_valid(curr_pass, required_fields, validators)
        if valid:
            valid_passports.append(curr_pass)
            if optional_field not in curr_pass:
                passports_without_cid.append(curr_pass)
        reading_pass = False
        # print(curr_pass, valid, len(curr_pass), optional_field in curr_pass)
        continue

    if not reading_pass:
        curr_pass = {}
        reading_pass = True

    data = line.split(' ')
    for field in data:
        header, field_data = field.split(':')
        curr_pass[header] = field_data

valid = is_valid(curr_pass, required_fields, validators)
if valid:
    valid_passports.append(curr_pass)
    if optional_field not in curr_pass:
        passports_without_cid.append(curr_pass)
    reading_pass = False
print(curr_pass, valid, len(curr_pass), optional_field in curr_pass)

print(len(valid_passports))
print(len(passports_without_cid)) 
