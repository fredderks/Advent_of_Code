instructions = open('input.txt', "r").read().split("\n")

operations = []
for line in instructions:
    prefix, suffix = line.split(" ")
    operations.append([prefix, suffix])


def decorrupt(input_list, start_index):
    instruction_list = [[op, arg] for op, arg in input_list]
    for index, instruction in enumerate(instruction_list[start_index:], start=start_index):
        if instruction[0] == "nop":
            instruction[0] = "jmp"
            instruction_list[index] = instruction
            break
        elif instruction[0] == "jmp":
            instruction[0] = "nop"
            instruction_list[index] = instruction
            break
    return instruction_list


def execute_instruction(index, instruction_list, accumulator):
    instruction = instruction_list[index]
    operation = instruction[0]
    argument = instruction[1]
    if operation == "nop":
        index += 1
    elif operation == "acc":
        accumulator += int(argument)
        index += 1
    else:
        index += int(argument)
    return index, accumulator


def program(instruction_list, part):
    input_list = instruction_list.copy()
    start_index = 0
    index = 0
    accumulator = 0
    index_list = []
    continue_loop = True
    while continue_loop:
        if index >= len(instruction_list):
            continue_loop = False
        elif index not in index_list: # if new instruction
            index_list.append(index)
            index, accumulator = execute_instruction(index, instruction_list, accumulator)
        elif part == "B": # if already been here
            instruction_list = decorrupt(input_list, start_index)
            start_index += 1
            index = 0
            accumulator = 0
            index_list = []
        elif part == "A":
            continue_loop = False
    return accumulator


# region --- Assignment 1 ---

print("accumulator:", program(operations, "A"))

# endregion
# region --- Assignment 2 ---

print("accumulator:", program(operations, "B"))

# endregion
