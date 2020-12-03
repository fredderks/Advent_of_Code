from collections import Counter
import matplotlib.pyplot as plt
import time


def read_map(file):
    input = open(file)
    map = []
    for line in input.readlines():
        line = str(line)
        line = line.replace("\n", "")
        line = list(line)
        map.append(line)
    return map


def asteroid_locations(map):
    map_length = len(map)
    map_width = len(map[0])
    locations = []
    for y in range(map_length):
        for x in range(map_width):
            if map[y][x] == '#':
                locations.append({'x': x, 'y': y})
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


def detect_asteroids(fractions, asteroid, all_asteroids):
    # finding new asteroids from the vantage point of current asteroid
    # solve linear function for each slope, find asteroids
    counter = 0
    up = 0
    down = 0
    for object in all_asteroids:
        if object['x'] == asteroid['x']:
            if object['y'] < asteroid['y']:
                up = 1
            elif object['y'] > asteroid['y']:
                down = 1
    for slope in fractions:
        intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
        minus = intercept - 0.0001
        plus = intercept + 0.0001
        objects_on_slope = []
        for object in all_asteroids:
            y = object['y']
            x = object['x']
            deriv_inter = (y + slope * x)
            # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
            if plus > deriv_inter > minus and x != asteroid['x']:
                # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
                sign = x - asteroid['x'] < 0
                objects_on_slope.append((slope, sign))
        counter += len(Counter([tuple(i) for i in objects_on_slope]))

    return counter + up + down

def map_best_locations(map):
    best = -1
    location = []
    counter = 0
    all_asteroids = asteroid_locations(map)
    for asteroid in all_asteroids:
        print(asteroid['x'], asteroid['y'])
        fractions = find_fractions(asteroid, map)
        detected = detect_asteroids(fractions, asteroid, all_asteroids)
        counter += 1
        if detected > best:
            best = detected
            location = asteroid
    print('Best location:', location, 'with', best, 'asteroids.', 'Total of', counter, 'asteroids')

#
# map = read_map('test.txt')
# # count number of asteroids
# t = time.process_time()
#
# map_best_locations(map)
#
# elapsed_time = time.process_time() - t
#
# print(round(elapsed_time, 2), 'seconds')

# #Correct answer: [28, 29]

# endregion


# region --- Assignment 2 ---

def closest_object(objects, direction, coordinate):
    if direction == 'min':
        expression = 'min('
    elif direction == 'max':
        expression = 'max('
    if coordinate == 'x':
        expression += 'objects, key=lambda t: t[0])'
    elif coordinate == 'y':
        expression += 'objects, key=lambda t: t[1])'
    # print(expression)
    return eval(expression)


def find_slopes(fractions, asteroid, all_asteroids):
    # finding new asteroids from the vantage point of current asteroid
    # solve linear function for each slope, find asteroids
    closest_asteroids = []

    # RIGHT
    up_objects = []
    for object in all_asteroids:
        if object['x'] == asteroid['x'] and object['y'] < asteroid['y']:
            up_objects.append((object['x'], object['y']))
    if up_objects:
        closest_on_up = closest_object(up_objects, 'max', 'y')
        closest_asteroids.append((closest_on_up[0], 0 - closest_on_up[1]))
    for slope in fractions:
        intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
        minus = intercept - 0.0001
        plus = intercept + 0.0001
        objects_on_slope = []
        for object in all_asteroids:
            y = object['y']
            x = object['x']
            if x >= asteroid['x']:
                deriv_inter = (y + slope * x)
                # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
                if plus > deriv_inter > minus and x != asteroid['x']:
                    # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
                    objects_on_slope.append((x, y))
        if objects_on_slope:
            closest_on_slope = closest_object(objects_on_slope, 'min', 'x')
            closest_asteroids.append((closest_on_slope[0], 0 - closest_on_slope[1]))

    # LEFT
    down_objects = []
    for object in all_asteroids:
        if object['x'] == asteroid['x'] and object['y'] > asteroid['y']:
            down_objects.append((object['x'], object['y']))
    if down_objects:
        closest_on_down = closest_object(down_objects, 'min', 'y')
        closest_asteroids.append((closest_on_down[0], 0 - closest_on_down[1]))
    for slope in fractions:
        intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
        minus = intercept - 0.0001
        plus = intercept + 0.0001
        objects_on_slope = []
        for object in all_asteroids:
            y = object['y']
            x = object['x']
            if x <= asteroid['x']:
                deriv_inter = (y + slope * x)
                # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
                if plus > deriv_inter > minus and x != asteroid['x']:
                    # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
                    objects_on_slope.append((x, y))
        if objects_on_slope:
            closest_on_slope = closest_object(objects_on_slope, 'max', 'x')
            closest_asteroids.append((closest_on_slope[0], 0 - closest_on_slope[1]))

    return closest_asteroids

t = time.process_time()
map = read_map('test.txt')
# map_length = len(map)
# map_width = len(map[0])

asteroid = {'x': 28, 'y': 29}

all_asteroids = asteroid_locations(map)
fractions = find_fractions(asteroid, map)
matches = find_slopes(fractions, asteroid, all_asteroids)
plot_x, plot_y = zip(*matches)

for i in [1, 2, 3, 10, 20, 50, 100, 199, 200, 201]:
    print(matches[i-1][0]*100 + (0-matches[i-1][1]))

elapsed_time = time.process_time() - t

print(round(elapsed_time, 3), 'seconds')

print("detected:", len(matches))
plt.plot(plot_x, plot_y)

plt.show()

# correct 2628
# endregion
