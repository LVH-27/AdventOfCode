def is_valid(passport, required_fields):
    valid = True
    for field in required_fields:
        if field not in passport:
           return False
    return True
 


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

valid_count = 0
valid_passports = []
passports_without_cid = []

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_field = "cid"

reading_pass = False
for line in lines:
    print(line)
    if len(line) == 0:
        valid = is_valid(curr_pass, required_fields)
        if valid:
            valid_passports.append(curr_pass)
            if optional_field not in curr_pass:
                passports_without_cid.append(curr_pass)
        reading_pass = False
        print(curr_pass, valid, len(curr_pass), optional_field in curr_pass)
        continue

    if not reading_pass:
        curr_pass = {}
        reading_pass = True

    data = line.split(' ')
    for field in data:
        header, field_data = field.split(':')
        curr_pass[header] = field_data

valid = is_valid(curr_pass, required_fields)
if valid:
    valid_passports.append(curr_pass)
    if optional_field not in curr_pass:
        passports_without_cid.append(curr_pass)
    reading_pass = False
print(curr_pass, valid, len(curr_pass), optional_field in curr_pass)

print(len(valid_passports))
print(len(passports_without_cid)) 
