expense_report = open('input.txt', "r").read().splitlines()

# region --- Assignment 1 ---

leftover_list = expense_report.copy()

for entry in expense_report:
    leftover_list.remove(entry)
    match_entry = str(2020 - int(entry))
    if match_entry in leftover_list:
        print(entry, "*", match_entry, "=", int(entry)*int(match_entry))

# region --- Assignment 2 ---

leftover_list = expense_report.copy()

for n1 in expense_report:
    leftover_list.remove(n1)
    sum2 = str(2020 - int(n1))
    for n2 in leftover_list:
        n3 = str(int(sum2) - int(n2))
        if n3 in leftover_list:
            print(n1, "*", n2, "*", n3, "=", int(n1)*int(n2)*int(n3))
            break
