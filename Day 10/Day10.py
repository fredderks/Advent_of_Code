from collections import Counter
import matplotlib.pyplot as plt
import time
import numpy
import operator


def read_map(file):
    input = open(file)
    map = []
    for line in input.readlines():
        line = str(line)
        line = line.replace("\n", "")
        line = list(line)
        map.append(line)
    return map


def asteroid_counter(map):
    counter = 0
    for y in map:
        counter += y.count('#')
    return counter


def asteroid_locations(map):
    map_length = len(map)
    map_width = len(map[0])
    locations = []
    for y in range(map_length):
        line = []
        for x in range(map_width):
            if map[y][x] == '#':
                locations.append((y, x))
    return locations


def find_fractions(asteroid, map):
    # find linear equations that work for this vantage point
    right = (len(map[0])) - asteroid['x']
    left = 0 - asteroid['x']
    down = asteroid['y'] - (len(map) - 1)
    up = asteroid['y']
    # print('Right:', right, ' Down:', down, " Left:", left, ' Up:', up)

    fractions = []

    for numerator in range(down, 0):
        for denominator in range(left, 0):
            fractions.append(numerator / denominator)
            # print(numerator, "/", denominator, sep="")
        for denominator in range(1, right):
            fractions.append(numerator / denominator)
            # print(numerator, "/", denominator, sep="")
    for numerator in range(up + 1):
        for denominator in range(left, 0):
            fractions.append(numerator / denominator)
            # print(numerator, "/", denominator, sep="")
        for denominator in range(1, right):
            fractions.append(numerator / denominator)
            # print(numerator, "/", denominator, sep="")

    fractions = list(set(fractions))
    fractions.sort(reverse=True)
    # print(fractions)
    return fractions


# region --- Assignment 1 ---

# def deriv_right_angles(asteroid_x, asteroid_y, map, map_length, map_width):
#     left = 0
#     right = 0
#     up = 0
#     down = 0
#     for x in range(0, asteroid_x):
#         if map[asteroid_y][x] == '#':
#             left = 1
#
#     for x in range(asteroid_x + 1, map_width):
#         if map[asteroid_y][x] == '#':
#             right = 1
#         # right_angles.append([x, asteroid_y])
#
#     for y in range(asteroid_y + 1, map_length):
#         if map[y][asteroid_x] == '#':
#             down = 1
#         # right_angles.append([asteroid_x, y])
#
#     for y in range(0, asteroid_y):
#         if map[y][asteroid_x] == '#':
#             up = 1
#         # right_angles.append([asteroid_x, y])
#     # print(left, right, up, down)
#     return sum([left, right, up, down])
#
#
#
# def find_slopes(fractions, asteroid, all_asteroids, map):
#     # finding new asteroids from the vantage point of current asteroid
#     # solve linear function for each slope, find asteroids
#     slopes = []
#     for slope in fractions:
#         intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
#         minus = intercept - 0.0001
#         plus = intercept + 0.0001
#         for object in all_asteroids:
#             y = object[0]
#             x = object[1]
#             deriv_inter = (y + slope * x)
#             # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
#             if plus > deriv_inter > minus and x != asteroid['x'] and y != asteroid['y']:
#                 # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
#                 sign = y - asteroid['y'] < 0
#                 slopes.append((slope, sign))
#     return slopes
#
#
# def map_best_locations(map):
#     map_length = len(map)
#     map_width = len(map[0])
#     best_locations = []
#     best = -1
#     location = []
#     counter = 0
#     all_asteroids = asteroid_locations(map)
#     for y in range(map_length):
#         line_locations = []
#         print('--- new line ---')
#         for x in range(map_width):
#             if map[y][x] == '#':
#                 asteroid = {'x': x, 'y': y}
#                 # print("--- finding fractions ---")
#                 fractions = find_fractions(asteroid, map)
#                 # print("--- finding slopes ---")
#                 unique_slopes = find_slopes(fractions, asteroid, all_asteroids, map)
#                 unique_slopes = Counter([tuple(i) for i in unique_slopes])
#                 # print("--- finding right angles ---")
#                 horivert = deriv_right_angles(asteroid['x'], asteroid['y'], map, map_length, map_width)
#                 # print('right angles:', horivert, ' from diagonals:', len(unique_slopes), ' total:',
#                 #       horivert + len(unique_slopes))
#                 counter += 1
#                 detected = horivert + len(unique_slopes)
#                 if detected > best:
#                     best = detected
#                     location = [x, y]
#                 line_locations.append(str(detected))
#             else:
#                 line_locations.append('.')
#         best_locations.append(line_locations)
#
#     for line in best_locations:
#         print(line)
#     print('Best location:', location, 'with', best, 'asteroids.', 'Total of', counter, 'asteroids')
#
#
# map = read_map('test.txt')
# # count number of asteroids
# number_asteroids = asteroid_counter(map)
#
# t = time.process_time()
#
# map_best_locations(map)
#
#
# elapsed_time = time.process_time() - t
#
#
#
# if elapsed_time > 60:
#     print(round(elapsed_time / 60, 2), 'minutes')
# else:
#     print(round(elapsed_time, 2), 'seconds')
# #Correct answer: [28, 29]
# # endregion


# region --- Assignment 2 ---

def find_slopes(fractions, asteroid, all_asteroids, map):
    # finding new asteroids from the vantage point of current asteroid
    # solve linear function for each slope, find asteroids
    points_x = []
    points_y = []
    slopes = []

    up_objects = []
    for object in all_asteroids:
        if object[1] == asteroid['x'] and object[0] < asteroid['y']:
            y = object[0]
            x = object[1]
            sign = y - asteroid['y'] < 0
            up_objects.append((x, y))
    if up_objects:
        print(up_objects)
        closest_on_up = max(up_objects, key=lambda t: t[1])
        # print(closest_on_up)
        points_x.append(closest_on_up[0])
        points_y.append(0 - closest_on_up[1])
    for slope in fractions:
        intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
        minus = intercept - 0.0001
        plus = intercept + 0.0001
        objects_on_slope = []
        for object in all_asteroids:
            y = object[0]
            x = object[1]
            if x >= asteroid['x']:
                deriv_inter = (y + slope * x)
                # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
                if plus > deriv_inter > minus and x != asteroid['x']:  # and y != asteroid['y']:
                    # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
                    sign = y - asteroid['y'] < 0
                    slopes.append((slope, sign))
                    objects_on_slope.append((x, y))
        if objects_on_slope:
            closest_on_slope = min(objects_on_slope, key=lambda t: t[0])
            # print(closest_on_slope)
            points_x.append(closest_on_slope[0])
            points_y.append(0 - closest_on_slope[1])
    down_objects = []
    for object in all_asteroids:
        if object[1] == asteroid['x'] and object[0] > asteroid['y']:
            y = object[0]
            x = object[1]
            sign = y - asteroid['y'] < 0
            down_objects.append((x, y))
    if down_objects:
        closest_on_down = min(down_objects, key=lambda t: t[1])
        # print(closest_on_down)
        points_x.append(closest_on_down[0])
        points_y.append(0 - closest_on_down[1])
    for slope in fractions:
        intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
        minus = intercept - 0.0001
        plus = intercept + 0.0001
        objects_on_slope = []
        for object in all_asteroids:
            y = object[0]
            x = object[1]
            if x <= asteroid['x']:
                deriv_inter = (y + slope * x)
                # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
                if plus > deriv_inter > minus and x != asteroid['x']:  # and y != asteroid['y']:
                    # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
                    sign = y - asteroid['y'] < 0
                    slopes.append((slope, sign))
                    objects_on_slope.append((x, y))
        if objects_on_slope:
            closest_on_slope = max(objects_on_slope, key=lambda t: t[0])
            # print(closest_on_slope)
            points_x.append(closest_on_slope[0])
            points_y.append(0 - closest_on_slope[1])
    plt.plot(points_x, points_y)

    plt.show()

    return points_x, points_y


map = read_map('test.txt')
map_length = len(map)
map_width = len(map[0])

asteroid = {'x': 28, 'y': 29}
all_asteroids = asteroid_locations(map)

fractions = find_fractions(asteroid, map)
matches_x, matches_y = find_slopes(fractions, asteroid, all_asteroids, map)

for i in [1, 2, 3, 10, 20, 50, 100, 199, 200, 201]:
    x = matches_x[i - 1]
    y = 0 - matches_y[i-1]
    print(i, ': ', 100*x+y, sep='')

# endregion
