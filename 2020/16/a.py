with open("input", 'r') as f:
    lines = [line.strip() for line in f.readlines()]

rules = {}
for i, line in enumerate(lines):
    if len(line) == 0:
        break
    field, rule = line.split(': ')
    rule_range = []
    for part in rule.split(" or "):
        start = int(part.split('-')[0])
        end = int(part.split('-')[1]) + 1
        rule_range.extend(list(range(start, end)))
    rules[field] = rule_range

my_ticket = lines[i + 2]
nearby_tickets_start = i + 5

invalid_fields = []
for ticket in lines[nearby_tickets_start:]:
    fields = [int(n.strip()) for n in ticket.split(',')]
    for field in fields:
        found_rule = False
        for rule in rules:
            if field in rules[rule]:
                found_rule = True
                break
        if not found_rule:
            invalid_fields.append(field)

print(sum(invalid_fields))

