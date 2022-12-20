import re


def priority_item(item):
    if item.islower():
        index = ord('a') - 1
    else:
        index = ord('A') - 27
    return ord(item) - index


# Part One
rucksacks = open('input.txt', "r").read().splitlines()

sum_priorities = 0
for rucksack in rucksacks:
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    common_item = ''.join(set(compartment1).intersection(compartment2))
    priority = priority_item(common_item)
    sum_priorities += priority

print(sum_priorities)

# Part Two
rucksacks = open('input.txt', "r").read()

groups = [x.splitlines() for x in re.findall('((?:[^\n]+\n?){1,3})', rucksacks)]

sum_priorities = 0
for group in groups:
    common_item = ''.join(set(group[0]).intersection(group[1], group[2]))
    priority = priority_item(common_item)
    sum_priorities += priority

print(sum_priorities)
