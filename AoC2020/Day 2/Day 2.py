import re

corrupted_passwords = open('input.txt', "r").read().splitlines()

# region --- Assignment 1 ---

counter = 0
for password_line in corrupted_passwords:
    clean_string = re.sub('\W+', ' ', password_line)
    range1, range2, pattern, password = clean_string.split()
    range1 = int(range1)
    range2 = int(range2)
    occurrences = len(re.findall(pattern, password))
    if range1 <= occurrences <= range2:
        counter = counter + 1
print(counter)

# endregion

# region --- Assignment 2 ---
counter = 0
for password_line in corrupted_passwords:
    clean_string = re.sub('\W+', ' ', password_line)
    index1, index2, pattern, password = clean_string.split()
    index1 = int(index1) - 1
    index2 = int(index2) - 1
    try:
        occurs_on_index1 = password[index1] == pattern
    except:
        occurs_on_index1 = False
        pass
    try:
        occurs_on_index2 = password[index2] == pattern
    except:
        occurs_on_index2 = False
        pass
    if bool(occurs_on_index1) != bool(occurs_on_index2):
        counter = counter + 1
print(counter)

# endregion