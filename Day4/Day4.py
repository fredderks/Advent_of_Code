# Your puzzle input is 387638-919123.

# region --- Assignment 1 ---
input_range = range(387638, 919123)

password_count = 0

for input in input_range:
    double = False
    increase = True
    previous = "-100"
    for char in str(input):
        if int(char) < int(previous): # Make sure the digit is higher than its left neighbour
            increase = False
        if previous == char:  # Make sure there are two identical adjacent digits
            double = True
        previous = char
    if double and increase:
        password_count += 1
print(" --- Assignment 1 --- \nNumber of valid passwords:", password_count)
# endregion

# region --- Assignment 2 ---
input_range = range(387638, 919123)

passwords = []

for input in input_range:
    double = False
    increase = True
    previous = "-100"
    for char in str(input):
        if int(char) < int(previous): # Make sure the digit is higher than its left neighbour
            increase = False
        if previous == char:  # Make sure there are two identical adjacent digits
            double = True
        previous = char
    if double and increase:
        passwords.append(input)

counter = 0

for password in passwords:
    previous = "-100"
    charlist = []
    for char in str(password):          # The distinct characters of the password is put into a list
        charlist += char
    distinct_char = list(set(charlist))
    if len(distinct_char) > 1:      # Discard passwords that only have one distinct digit, like: 444444
        double = False
        for i in distinct_char:
            count = charlist.count(i)
            if count == 2:          # If a distinct character is found exactly twice, the password is valid
                double = True
        if double:
            # print("Valid! -", password)
            counter += 1

print(" --- Assignment 2 --- \nNumber of valid passwords:", counter)
# endregion
