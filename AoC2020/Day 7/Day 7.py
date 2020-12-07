import re

rules = open('input.txt', "r").read().split("\n")

rules_dict = {}

for line in rules:
    prefix, suffix = line.split(" contain ")
    outer_bag = re.sub(r" bag[s]?", "", prefix)
    inner_bags = re.sub(r" bag[s]?[.]?", "", suffix)
    inner_bags = [string.split(" ", 1) for string in inner_bags.split(", ") if "no" not in string]
    rules_dict[outer_bag] = inner_bags

# region --- Assignment 1 ---


def contain_bag(current_colour, ultimate_colour):
    if ultimate_colour == current_colour:
        return True
    else:
        return any(contain_bag(colour, ultimate_colour) for _, colour in rules_dict[current_colour])


def number_bags_contain(bag_colour):
    total = 0
    for colour in rules_dict.keys():
        if colour != bag_colour:
            total += contain_bag(colour, bag_colour)
    return total


print(number_bags_contain("shiny gold"))

# endregion
# region --- Assignment 2 ---


def number_bags_contained(bag_colour):
    if not rules_dict[bag_colour]:
        return False
    else:
        total = 0
        for num, colour in rules_dict[bag_colour]:
            total += int(num) + (int(num) * number_bags_contained(colour))
        return total


print(number_bags_contained("shiny gold"))

# endregion
