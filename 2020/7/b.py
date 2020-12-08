import re


def count_bags(rule, rules, prefix=""):
    bag = rule[1]
    multiplier = rule[0]
    if len(rules[bag]) == 0:
        return multiplier
    
    bag_count = multiplier 
    for inner_bag in rules[bag]:
        # if len(rules[inner_bag[1]]) == 0:
        #    bag_count += inner_bag[0]
        recursive_bag_count = count_bags(inner_bag, rules, prefix + '\t')
        bag_count += multiplier * recursive_bag_count
        # print(inner_bag, 
    return bag_count


with open("input", "r") as f:
    lines = f.readlines()

my_bag = "shiny gold"
rules = {}
bagex = re.compile("([0-9]+) ([a-z]+ [a-z]+) bags?")

for line in lines:
    rule = line.split(" contain ")
    outer_bag = rule[0][:-5]
    inner_bags = bagex.findall(rule[1])
    if not inner_bags:
        inner_bags = []
    rules[outer_bag] = [(int(bag[0]), bag[1]) for bag in inner_bags]

total_bag_count = 0

for rule in rules[my_bag]:
    total_bag_count += count_bags(rule, rules)

print(total_bag_count) 


