import re


def my_bag_allowed(rule, my_bag, rules):
    colors = [bag[1] for bag in rules[rule]]
    if my_bag in colors:
        return True
    for inner_rule in colors:
        if my_bag_allowed(inner_rule, my_bag, rules):
            return True
    return False


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
    rules[outer_bag] = inner_bags

color_candidates = []

for rule in rules:
    if my_bag_allowed(rule, my_bag, rules):
       color_candidates.append(rule)

print(len(color_candidates)) 


