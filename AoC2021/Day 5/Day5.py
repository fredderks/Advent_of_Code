import numpy as np
from collections import Counter


def intermediate_points(start_coords, end_coords, include_diag=False):
    x1, y1 = start_coords
    x2, y2 = end_coords
    intermediates_list = []
    if x1 == x2:  # vertical
        for y_point in range(y1, y2 + np.sign(y2-y1), np.sign(y2-y1)):
            intermediates_list.append((x1, y_point))
    elif y1 == y2:  # horizontal
        for x_point in range(x1, x2 + np.sign(x2-x1), np.sign(x2-x1)):
            intermediates_list.append((x_point, y1))
    elif include_diag:  # diagonal
        for x_point, y_point in zip(range(x1, x2 + np.sign(x2-x1), np.sign(x2-x1)), range(y1, y2 + np.sign(y2-y1), np.sign(y2-y1))):
            intermediates_list.append((x_point, y_point))
    else:
        pass
    return intermediates_list


vents_input = open('input.txt', "r").read().splitlines()
input_coordinates = []
for line in vents_input:
    start, end = line.split(" -> ")
    input_coordinates.append([[int(i) for i in start.split(",")], [int(j) for j in end.split(",")]])

# region --- Assignment 1 ---


full_coordinates = []
for line in input_coordinates:
    full_coordinates.extend(intermediate_points(line[0], line[1]))

count_dict = Counter(full_coordinates)
number_overlaps = len([i for i in count_dict.values() if i > 1])
print(f"Horizontal and vertical lines overlap at {number_overlaps} points")

# endregion

# region --- Assignment 2 ---

full_coordinates = []
for line in input_coordinates:
    full_coordinates.extend(intermediate_points(line[0], line[1], True))

count_dict = Counter(full_coordinates)
number_overlaps = len([i for i in count_dict.values() if i > 1])
print(f"Horizontal, vertical and diagonal lines overlap at {number_overlaps} points")

# endregion
