worksheet_input = open('input.txt', "r").read().splitlines()


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


worksheet = []
for line in worksheet_input:
    worksheet.append(line.split())

transposed_worksheet = transpose(worksheet)

row_total = 0
for row in transposed_worksheet:
    if row[-1] == "*":
        prod = 1
        for i in row[:-1]:
            prod = prod * int(i)
    else:
        prod = sum([int(i) for i in row[:-1]])
    # print(row[:-1], prod)
    row_total += prod

print('grand total for part 1:', row_total)

# Part 2 #
transposed_worksheet = transpose(worksheet_input)

total_sum = 0
problem_sum = 0
for line in transposed_worksheet:
    line_str = ''.join(line[:-1]).strip()
    if line_str:  # valid number
        number = int(line_str)
        if line[-1] == '*' or line[-1] == '+':
            modifier = line[-1]
        if problem_sum == 0:
            problem_sum = number
        else:
            problem_sum = problem_sum * number if modifier == '*' else problem_sum + number
    else:  # new problem
        total_sum += problem_sum
        problem_sum = 0
        modifier = ''

total_sum += problem_sum
print('grand total for part 2:', total_sum)
