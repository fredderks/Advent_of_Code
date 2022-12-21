signal = open('input.txt', "r").read()


def start_of_substring(string, length):
    substring = ""
    iteration = 0
    for char in string:
        iteration += 1
        substring += char
        substring = substring[-length:]
        if len(set(substring)) == length:
            print(substring, iteration)
            break


start_of_substring(signal, 4)   # Part One
start_of_substring(signal, 14)  # Part Two
