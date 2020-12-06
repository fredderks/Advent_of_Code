import collections
custom_declarations = open('input.txt', "r").read().split("\n\n")



# region --- Assignment 1 ---

# custom_declarations = [line.replace("\n", "") for line in custom_declarations]
# set_input = [len(set(line)) for line in custom_declarations]
# print(custom_declarations)
# print(sum(set_input))

# endregion
# region --- Assignment 2 ---

custom_declarations = [line.replace("\n", " ") for line in custom_declarations]
totalquestions = []
for group in custom_declarations:
    group = group.split()
    groupcount = len(group) - 1
    if len(group) > 1:
        grouplist = []
        for person in group:
            person_list = list(person)
            [grouplist.append(question) for question in person_list]
        questionseveryone = [item for item, count in collections.Counter(grouplist).items() if count > groupcount]
        totalquestions.append(len(questionseveryone))
    else:
        totalquestions.append(len(group[0]))

print(totalquestions)
print("sum of counts:", sum(totalquestions))

# endregion
