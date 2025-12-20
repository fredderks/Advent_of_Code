rotation_instructions = open('input.txt', "r").read().splitlines()

times_zero = 0
start_position = 50

for rotation in rotation_instructions:
    direction, digits = rotation[0], int(rotation[1:])
    times = 0

    if direction == 'L':
        position = start_position - digits
    else:
        position = start_position + digits

    if position <= 0 or position >= 100:
        times = int(abs(position / 100))
        if start_position != 0 and position <= 0:
            times += 1
    start_position = position % 100
    times_zero = times_zero + times

print("times zero:", times_zero)
