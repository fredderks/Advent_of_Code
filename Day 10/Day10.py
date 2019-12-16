from collections import Counter


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


def deriv_right_angles(asteroid_x, asteroid_y, map):
    map_length = len(map)
    map_width = len(map[0])
    counter = 0
    left = 0
    right = 0
    up = 0
    down = 0
    for x in range(0, asteroid_x):
        if map[asteroid_y][x] == '#':
            left = 1

    for x in range(asteroid_x + 1, map_width):
        if map[asteroid_y][x] == '#':
            right = 1
        # right_angles.append([x, asteroid_y])

    for y in range(asteroid_y + 1, map_length):
        if map[y][asteroid_x] == '#':
            down = 1
        # right_angles.append([asteroid_x, y])

    for y in range(0, asteroid_y):
        if map[y][asteroid_x] == '#':
            up = 1
        # right_angles.append([asteroid_x, y])
    # print(left, right, up, down)
    return sum([left, right, up, down])


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
    for numerator in range(up+1):
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


def find_slopes(fractions, asteroid, map):
    # finding new asteroids from the vantage point of current asteroid
    # solve linear function for each slope, find asteroids
    map_length = len(map)
    map_width = len(map[0])
    slopes = []

    for slope in fractions:
        intercept = asteroid['y'] + slope * asteroid['x']  # intercept for the linear function give the current slope
        minus = intercept - 0.0001
        plus = intercept + 0.0001
        for y in range(map_length):
            for x in range(map_width):
                deriv_inter = (y + slope * x)
                # print(map[y][x], 'slope:', slope,'intercept:',intercept, 'deriv_inter', deriv_inter)
                if map[y][x] == '#' and plus > deriv_inter > minus and x != asteroid['x'] and y != asteroid['y']:
                    # print('x:', x, 'y:', y, 'slope:', slope, 'intercept:', y + slope * x, y - asteroid['y'])
                    sign = y - asteroid['y'] < 0
                    slopes.append((slope, sign))
    return slopes


def map_best_locations(map):
    best_locations = []
    best = -1
    location = []
    counter = 0
    for y in range(map_length):
        line_locations = []
        for x in range(map_width):
            if map[y][x] == '#':
                asteroid = {'x': x, 'y': y}
                fractions = find_fractions(asteroid, map)
                unique_slopes = find_slopes(fractions, asteroid, map)
                unique_slopes = Counter([tuple(i) for i in unique_slopes])
                horivert = deriv_right_angles(asteroid['x'], asteroid['y'], map)
                # print('right angles:', horivert, ' from diagonals:', len(unique_slopes), ' total:',
                #       horivert + len(unique_slopes))
                counter  += 1
                detected = horivert + len(unique_slopes)
                if detected > best:
                    best = detected
                    location = [x,y]
                line_locations.append(str(detected))
            else:
                line_locations.append('.')
        best_locations.append(line_locations)

    for line in best_locations:
        print(line)
    print('Best location:', location, 'with', best, 'asteroids.', 'Total of', counter, 'asteroids')


map = read_map('test.txt')
map_length = len(map)
map_width = len(map[0])
min_step = 1 / map_width
max_step = map_length

# ---
# count number of asteroids
number_asteroids = asteroid_counter(map)

map_best_locations(map)


# asteroid = {'x': 0, 'y': 2}
# # print(map[asteroid['y']][asteroid['x']])
#
# fractions = find_fractions(asteroid, map)
#
# unique_slopes = find_slopes(fractions, asteroid, map)
# unique_slopes = Counter([tuple(i) for i in unique_slopes])
# print(unique_slopes)
#
# horivert = deriv_right_angles(asteroid['x'], asteroid['y'], map)
# print('right angles:', horivert, ' from diagonals:', len(unique_slopes), ' total:', horivert + len(unique_slopes))
