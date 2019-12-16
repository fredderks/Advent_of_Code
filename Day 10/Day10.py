import math


def read_map(file):
    input = open(file)
    map = []
    for line in input.readlines():
        line = str(line)
        line = line.replace("\n", "")
        line = list(line)
        map.append(line)
    return map


map = read_map('test.txt')
map_length = len(map)
map_width = len(map[0])
min_step = 1 / map_width
max_step = map_length


def asteroid_counter(map):
    counter = 0
    for y in map:
        counter += y.count('#')
    return counter


def deriv_right_angles(asteroid_x, asteroid_y):
    right_angles = []
    for x in range(0, asteroid_x):
        right_angles.append([x, asteroid_y])

    for x in range(asteroid_x + 1, map_width):
        right_angles.append([x, asteroid_y])

    for y in range(asteroid_y + 1, map_length):
        right_angles.append([asteroid_x, y])

    for y in range(0, asteroid_y):
        right_angles.append([asteroid_x, y])

    return right_angles


# ---

asteroid = {'x': 1, 'y': 0}
# print(map[asteroid['y']][asteroid['x']])
# count number of asteroids
number_asteroids = asteroid_counter(map)

# find linear equations that work for this vantage point
right = map_width - asteroid['x']
left = 0 - asteroid['x']
up = asteroid['y']
down = asteroid['y'] - map_length
print('Right:', right, ' Down:', down, " Left:", left, ' Up:', up)
# first quarter
# calculate all possible slopes (for first quarter) #TODO find slopes for full hemisphere
fractions = []
for numerator in range(1 + down, 0):
    for denominator in range(1, right):
        fractions.append(numerator / denominator)
        # print(numerator, denominator)
for numerator in range(1 + down, 0):
    for denominator in range(left, 0):
        fractions.append(numerator / denominator)
fractions = list(set(fractions))
fractions.sort(reverse=True)
print(fractions)
print()
# finding new asteroids from the vantage point of current asteroid
# solve linear function for each slope, find asteroids

slope = fractions[6]
slopes = []

for slope in fractions:
    intercept = asteroid['y'] - slope * asteroid['x']        # intercept for the linear function give the current slope
    minus = intercept - 0.0001
    plus = intercept + 0.0001
    for y in range(map_length):
        for x in range(map_width):
            deriv_inter = (0 - y - slope * x)
            if map[y][x] == '#' and plus > deriv_inter > minus and x != asteroid['x'] and y != asteroid['y']:
                # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', 0 - y - slope * x)
                slopes.append(slope)

horivert = deriv_right_angles(asteroid['x'], asteroid['y'])

# print(list(set(slopes)))

# print(1/4)

# print(map[y][x])
