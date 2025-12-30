manifold = open('input.txt', "r").read().splitlines()

# Part 2 #
splits = 0
for i in range(len(manifold), 0, -1):
    row = i - 1
    line = manifold[row]
    for col in range(len(line)):
        if line[col] == '^':
            upper_row = row - 2
            while upper_row >= 0:
                triplet = manifold[upper_row][col - 1 : col + 2]
                if triplet[1] == '^':
                    break
                if triplet[0] == '^' or triplet[2] == '^' or triplet[1] == 'S':
                    splits += 1
                    break
                else:
                    upper_row -= 2

print('total splits:', splits)

# Part 2 #
matrix = [list(line) for line in manifold]


def set_adjacent_cell(matrix, row, col, offset, value):
    # Adds value to adjacent cell, combines with existing value and inherits any existing vertical value. #
    adj_col = col + offset
    result = value

    # already has number on adjacent cell?
    if isinstance(matrix[row][adj_col], int):
        result += matrix[row][adj_col]

    # search upward for existing value to inherit
    upper_row = row - 2
    while upper_row >= 0:
        if isinstance(matrix[upper_row][adj_col], int):
            result += matrix[upper_row][adj_col]
            matrix[upper_row][adj_col] = '.'
            break
        upper_row -= 2

    matrix[row][adj_col] = result


def replace_matrix(matrix, row, col):
    upper_row = row - 2  # index of cell directly above
    while upper_row >= 0:
        cell = matrix[upper_row][col]
        if isinstance(cell, int):  # inherited number from above
            value = cell
            break
        elif cell == '^':
            value = 0
            break
        elif cell == 'S':
            value = 1
            break
        else:
            upper_row -= 2

    set_adjacent_cell(matrix, row, col, -1, value)  # set left adjacent cell
    set_adjacent_cell(matrix, row, col, 1, value)  # set right adjacent cell

    matrix[upper_row][col] = '.'  # replace parent cell now that it has been included in the sum,
    return matrix


for row in range(0, len(matrix), 2):
    line = matrix[row]
    for col in range(len(line)):
        if line[col] == '^':
            replace_matrix(matrix, row, col)

total_paths = sum(x for row in matrix for x in row if isinstance(x, int))

print('total paths:', total_paths)
