import math


def create_big_tree_map(small_map, slope):
    count = len(small_map)
    length = len(small_map[0])
    ratio = count / length
    index = 0
    big_map = []
    for row in tree_map:
        big_row = row * math.ceil(ratio * slope)
        big_map.append(big_row)
        index += 1
    return big_map


def plot_toboggan_slope(small_map, right, down):
    big_map = create_big_tree_map(small_map, right / down)
    line_count = len(big_map)
    trees_counted = 0
    pos = [0, 0]
    for line in range(line_count - 1):
        pos = [pos[0] + right, pos[1] + down]
        if pos[1] > line_count:
            break
        tree = big_map[pos[1]][pos[0]]
        # print(pos, tree)
        if tree == '#':
            trees_counted += 1
    return trees_counted


tree_map = open('input.txt', "r").read().splitlines()


# region --- Assignment 1 ---

print(plot_toboggan_slope(tree_map, right=3, down=1))

# endregion

# region --- Assignment 2 ---

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

trees_product = 1
for slope in slopes:
    trees = plot_toboggan_slope(tree_map, right=slope[0], down=slope[1])
    trees_product *= trees

print(trees_product)

# endregion
