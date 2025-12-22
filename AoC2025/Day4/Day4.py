grid_input = open('input.txt', "r").read().splitlines()

paper_matrix = [list(row) for row in grid_input]


def adjacent_coordinates(coords, bounds):
    row, col = coords
    row_bounds, col_bounds = bounds
    adjacents_template = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    adjacents = []
    for adjacent in adjacents_template:
        if row_bounds >= (adjacent[0] + row) >= 0 and col_bounds >= (adjacent[1] + col) >= 0:
            adjacents.append([adjacent[0] + row, adjacent[1] + col])
    return adjacents


PartTwo = True

rolls_accessible = 0
while True:
    new_rolls_accessible = 0
    row_index = 0
    for row in paper_matrix:
        column_index = 0
        for column in row:
            if column == '@':
                adjacents = adjacent_coordinates([row_index, column_index], [len(paper_matrix[0]) - 1, len(paper_matrix) - 1])
                paper_rolls = 0
                for adjacent in adjacents:
                    if paper_matrix[adjacent[0]][adjacent[1]] == '@':
                        paper_rolls += 1
                    if paper_rolls >= 4:
                        break
                if paper_rolls < 4:
                    new_rolls_accessible += 1
                    if PartTwo:
                        paper_matrix[row_index][column_index] = 'x'
            column_index += 1
        row_index += 1
    if new_rolls_accessible != 0:
        rolls_accessible += new_rolls_accessible
        if not PartTwo:
            break
    else:
        break

print(rolls_accessible)