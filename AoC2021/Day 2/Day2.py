planned_course = open('input.txt', "r").read().splitlines()

# region --- Assignment 1 ---

horizontal_pos = 0
depth = 0

for step in planned_course:
    command, distance = step.split(" ")
    distance = int(distance)
    if command == 'forward':
        horizontal_pos += distance
    elif command == 'down':
        depth += distance
    else:
        depth -= distance

product = horizontal_pos * depth
print(f"You have a horizontal position of {horizontal_pos} and a depth of {depth}. "
      f"(Multiplying these together produces {product}.)")


# endregion

# region --- Assignment 2 ---

horizontal_pos = 0
aim = 0
depth = 0

for step in planned_course:
    command, value = step.split(" ")
    value = int(value)
    if command == 'forward':
        horizontal_pos += value
        depth += aim * value
    elif command == 'down':
        aim += value
    else:
        aim -= value

product = horizontal_pos * depth
print(f"You have a horizontal position of {horizontal_pos} and a depth of {depth}. "
      f"(Multiplying these together produces {product}.)")


# endregion