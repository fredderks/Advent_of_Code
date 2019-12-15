file = open('input.txt', 'r')
file = file.readlines()[0]
code_str = list(file.split(','))
code = [int(i) for i in code_str]
print(code)

# region --- Assignment 1 ---
intcode = code.copy()
# intcode_list1[1] = 12
# intcode_list1[2] = 2
# print(max(code))


# for i in range(0, len(intcode_list1), 4):
i = 0
while True:
    instruction = intcode[i]
    print("instruction:", instruction, '- at index:', intcode.index(instruction))
    if instruction == 1:
        intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
        i += 4
        continue
    if instruction == 2:
        intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
        i += 4
        continue
    if instruction == 3:
        result = int(input('Please provide test input: '))
        intcode[intcode[i + 1]] = result                    # stores your input at the index given by the parameter
        i += 2
        continue
    elif instruction == 4:
        print(intcode[intcode[i + 2]])
        i += 2
        continue
    elif instruction == 99:
        break
    else:
        print('Parameter mode time!')
        instruction = str(instruction)
        opcode = int(instruction[-2:])
        param1_mode = int(instruction[-3])
        param2_mode = int(instruction[-4])
        if len(instruction) > 4:
            param3_mode = int(instruction[-5])
        else:
            param3_mode = 0

        # print('Opcode:',opcode,"param1",param1_mode,"param2",param2_mode,"param3",param3_mode)
        if not param1_mode:
            param1 = intcode[intcode[i + 1]]
        elif param1_mode:
            param1 = intcode[i + 1]
        if not param2_mode:
            param2 = intcode[intcode[i + 2]]
        elif param2_mode:
            param2 = intcode[i + 2]

        # print('param1',param1,'param2',param2)

        if opcode == 1:
            result = param1 + param2
            if not param3_mode:
                intcode[intcode[i + 3]] = result
            elif param3_mode:
                intcode[i + 3] = result
            i += 4
            continue
        elif opcode == 2:
            result = param1 * param2
            if not param3_mode:
                intcode[intcode[i + 3]] = result
            elif param3_mode:
                intcode[i + 3] = result
            i += 4
            continue
        else:
            break
print(" --- Assignmnent 1 --- ")
print(intcode)
# Correct: 2842648
# endregion