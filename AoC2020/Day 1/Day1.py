expense_report = open('input.txt', "r").read().splitlines()

# region --- Assignment 1 ---

leftover_list = expense_report.copy()

for entry in expense_report:
    leftover_list.remove(entry)
    match_entry = str(2020 - int(entry))
    if match_entry in leftover_list:
        print(entry, "*", match_entry, "=", int(entry)*int(match_entry))
