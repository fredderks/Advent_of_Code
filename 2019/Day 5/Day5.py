file = open('input.txt', 'r')
file = file.readlines()[0]
code_str = list(file.split(','))
code = [int(i) for i in code_str]
print(code)

# region --- Assignment 1 ---
print(" --- Assignmnent 1 --- ")
intcode = code.copy()

i = 0

def get_param1(mode):
    if not mode:
        param1 = intcode[intcode[i + 1]]
    elif mode and instr_len > 2:
        param1 = intcode[i + 1]
    return param1

def get_param2(mode):
    if not mode:
        param2 = intcode[intcode[i + 2]]
    elif mode and instr_len > 3:
        param2 = intcode[i + 2]
    return param2

# while True:
#     param1_mode = 0
#     param2_mode = 0
#     param3_mode = 0
#     instruction = intcode[i]
#     # print("instruction:", instruction, 'at index:', intcode.index(instruction), end = "")
#     instruction = str(instruction)
#     instr_len = len(instruction)
#     opcode = int(instruction[-2:])
#     if instr_len > 2:
#         param1_mode = int(instruction[-3])
#     if instr_len > 3:
#         param2_mode = int(instruction[-4])
#     if instr_len > 4:
#         param3_mode = int(instruction[-5])
#     # print(" - opcode:", opcode, "  C:", param1_mode, "  B:", param2_mode, "  A:", param3_mode)
#
#     if opcode == 1:
#         param1 = get_param1(param1_mode)
#         param2 = get_param2(param2_mode)
#         result = param1 + param2
#         if not param3_mode:
#             intcode[intcode[i + 3]] = result
#         elif param3_mode:
#             intcode[i + 3] = result
#         i += 4
#         continue
#
#     elif opcode == 2:
#         param1 = get_param1(param1_mode)
#         param2 = get_param2(param2_mode)
#         result = param1 * param2
#         if not param3_mode:
#             intcode[intcode[i + 3]] = result
#         elif param3_mode:
#             intcode[i + 3] = result
#         i += 4
#         continue
#
#     elif opcode == 3:
#         result = int(input('Please provide test input: '))
#         intcode[intcode[i + 1]] = result
#         i += 2
#         continue
#
#     elif opcode == 4:
#         param1 = get_param1(param1_mode)
#         if param1 == 0:
#             print("The test was successful!")
#         else:
#             print("Output code:",param1)
#         i += 2
#         continue
#
#     elif opcode == 99:
#         break
#
#     else:
#         print(opcode, "is not a valid opcode")
#         break

# correct: 9961446
# endregion

# region --- Assignment 2 ---
print(" --- Assignmnent 2 --- ")
while True:
    param1_mode = 0
    param2_mode = 0
    param3_mode = 0
    instruction = intcode[i]
    # print("instruction:", instruction, 'at index:', intcode.index(instruction), end = "")
    instruction = str(instruction)
    instr_len = len(instruction)
    opcode = int(instruction[-2:])
    if instr_len > 2:
        param1_mode = int(instruction[-3])
    if instr_len > 3:
        param2_mode = int(instruction[-4])
    if instr_len > 4:
        param3_mode = int(instruction[-5])
    # print(" - opcode:", opcode, "  C:", param1_mode, "  B:", param2_mode, "  A:", param3_mode)

    if opcode == 1:
        param1 = get_param1(param1_mode)
        param2 = get_param2(param2_mode)
        result = param1 + param2
        if not param3_mode:
            intcode[intcode[i + 3]] = result
        elif param3_mode:
            intcode[i + 3] = result
        i += 4
        continue

    elif opcode == 2:
        param1 = get_param1(param1_mode)
        param2 = get_param2(param2_mode)
        result = param1 * param2
        if not param3_mode:
            intcode[intcode[i + 3]] = result
        elif param3_mode:
            intcode[i + 3] = result
        i += 4
        continue

    elif opcode == 3:
        result = int(input('Please provide test input: '))
        intcode[intcode[i + 1]] = result
        i += 2
        continue

    elif opcode == 4:
        param1 = get_param1(param1_mode)
        print("Output code:", param1)
        i += 2
        continue

    elif opcode == 5:
        param1 = get_param1(param1_mode)
        param2 = get_param2(param2_mode)
        if param1 != 0:
            i = param2
        else:
            i += 3
        continue

    elif opcode == 6:
        param1 = get_param1(param1_mode)
        param2 = get_param2(param2_mode)
        if param1 == 0:
            i = param2
        else:
            i += 3
        continue

    elif opcode == 7:
        param1 = get_param1(param1_mode)
        param2 = get_param2(param2_mode)

        if param1 < param2:
            store = 1
        else:
            store = 0
        if not param3_mode:
            intcode[intcode[i + 3]] = store
        elif param3_mode:
            intcode[i + 3] = store
        i += 4
        continue

    elif opcode == 8:
        param1 = get_param1(param1_mode)
        param2 = get_param2(param2_mode)

        if param1 == param2:
            store = 1
        else:
            store = 0
        if not param3_mode:
            intcode[intcode[i + 3]] = store
        elif param3_mode:
            intcode[i + 3] = store
        i += 4
        continue

    elif opcode == 99:
        print("Halting the program!")
        break

    else:
        print(opcode, "is not a valid opcode")
        break
# endregion