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

tickets = lines[nearby_tickets_start:]
valid_tickets = []
for i, ticket in enumerate(tickets):
    fields = [int(n.strip()) for n in ticket.split(',')]
    ticket_valid = True

    for field in fields:
        found_rule = False
        for rule in rules:
            if field in rules[rule]:
                found_rule = True
                break
        if not found_rule:
            ticket_valid = False
            break
    if ticket_valid:
        valid_tickets.append([int(n.strip()) for n in ticket.split(',')])

my_ticket = [int(n.strip()) for n in my_ticket.split(',')]

rule_order = {}
possible_rules = [rule for rule in rules]
# go field by field and remove offending rules
while len(rule_order) < len(my_ticket):
    for i in range(len(my_ticket)):
        current_field_rules = list(possible_rules)
        rule_idx = 0
        while rule_idx < len(current_field_rules):
            rule = current_field_rules[rule_idx]
            for ticket in valid_tickets:
                if ticket[i] not in rules[rule]:
                    current_field_rules.remove(rule)
                    rule_idx -= 1  # move the index one step back, so that the regular increment keeps it in its place
                    break  # a ticket violating that rule-position pair was found
            rule_idx += 1
        if len(current_field_rules) == 1:
            rule_order[current_field_rules[0]] = i
            possible_rules.remove(current_field_rules[0])

print(rule_order)

prod = 1
for rule in rule_order:
    if "departure" in rule:
        prod *= my_ticket[rule_order[rule]]
print(prod)
