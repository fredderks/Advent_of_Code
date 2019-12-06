intcode_list = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 6, 23, 2, 13, 23, 27, 1, 27, 13,
                 31, 1, 9, 31, 35, 1, 35, 9, 39, 1, 39, 5, 43, 2, 6, 43, 47, 1, 47, 6, 51, 2, 51, 9, 55, 2, 55, 13, 59,
                 1, 59, 6, 63, 1,
                 10, 63, 67, 2, 67, 9, 71, 2, 6, 71, 75, 1, 75, 5, 79, 2, 79, 10, 83, 1, 5, 83, 87, 2, 9, 87, 91, 1, 5,
                 91, 95, 2, 13, 95, 99, 1, 99, 10, 103, 1, 103, 2, 107, 1, 107, 6, 0, 99, 2, 14, 0, 0]

# region --- Assignment 1 ---
intcode_list1 = intcode_list.copy()
intcode_list1[1] = 12
intcode_list1[2] = 2

for i in range(0, len(intcode_list1), 4):
    if intcode_list1[i] == 1:
        intcode_list1[intcode_list1[i + 3]] = intcode_list1[intcode_list1[i + 1]] + intcode_list1[intcode_list1[i + 2]]
    if intcode_list1[i] == 2:
        intcode_list1[intcode_list1[i + 3]] = intcode_list1[intcode_list1[i + 1]] * intcode_list1[intcode_list1[i + 2]]
    if intcode_list1[i] == 99:
        break
print(" --- Assignmnent 1 --- ")
print("Value at position 0:", intcode_list1[0])
# Correct: 2842648
# endregion

# region --- Assignment 2 ---
for noun in range(0, 99):
    for verb in range(0, 99):
        intcode_list2 = intcode_list.copy()
        intcode_list2[1] = noun
        intcode_list2[2] = verb
        for i in range(0, len(intcode_list2), 4):
            if intcode_list2[i] == 1:
                intcode_list2[intcode_list2[i + 3]] = intcode_list2[intcode_list2[i + 1]] + intcode_list2[intcode_list2[i + 2]]
            elif intcode_list2[i] == 2:
                intcode_list2[intcode_list2[i + 3]] = intcode_list2[intcode_list2[i + 1]] * intcode_list2[intcode_list2[i + 2]]
            elif intcode_list2[i] == 99:
                break
            else:
                break
        if intcode_list2[0] == 19690720:
            print(" --- Assignmnent 2 --- ")
            print("At zero:", intcode_list2[0])
            print("Noun + verb: " + str(noun) + str(verb))
# Correct: 9074
# endregion
