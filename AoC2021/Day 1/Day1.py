sonar_sweep = open('input.txt', "r").read().splitlines()

# region --- Assignment 1 ---

times_increased = 0

previous_depth = 0
for depth in sonar_sweep:
    depth = int(depth)
    if depth > previous_depth != 0:
        times_increased += 1
    # print(f'previous depth = {previous_depth}, current depth = {depth}, times increased = {times_increased}')
    previous_depth = depth

print(f'times increased = {times_increased}')

# endregion

# region --- Assignment 2 ---

times_increased = 0

current_window = []
for depth in sonar_sweep:
    depth = int(depth)
    if len(current_window) < 3:
        current_window.append(depth)
    else:
        previous_window = current_window.copy()
        current_window.pop(0)
        current_window.append(depth)
        # print(previous_window, sum(previous_window), current_window, sum(current_window))
        if sum(current_window) > sum(previous_window):
            times_increased += 1

print(f'times increased = {times_increased}')

# endregion