import numpy as np

diagnostic_report = open('input.txt', "r").read().splitlines()
transposed_report = []
for i in range(len(diagnostic_report[0])):
    transposed_report.append([row[i] for row in diagnostic_report])

# region --- Assignment 1 ---

gamma_rate = ""
epsilon_rate = ""

for bit in transposed_report:
    most_common = max(set(bit), key=bit.count)
    least_common = min(set(bit), key=bit.count)
    gamma_rate += most_common
    epsilon_rate += least_common

gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)
print(f"gamma rate: {gamma_rate} ({gamma_rate_dec}), epsilon rate: {epsilon_rate} ({epsilon_rate_dec}), "
      f"power consumption: {gamma_rate_dec * epsilon_rate_dec}")

# endregion

# region --- Assignment 2 ---

transposed_report = np.array(transposed_report)


def find_bit_criteria(array, mode):
    bincount = np.bincount(array)
    if len(bincount) == 2:
        x, y = bincount
        if mode == "O2":
            if x == y:
                return 1
            else:
                return np.bincount(array).argmax()
        else:
            if x == y:
                return 0
            else:
                return np.bincount(array).argmin()
    else:
        return bincount.argmax()


def find_life_support_rating(report, mode, k):
    bit = report[k]
    bit_criteria = find_bit_criteria(bit, mode)
    sliced_report = report[:, bit == bit_criteria]
    if len(sliced_report[0]) > 1:
        decimal = find_life_support_rating(sliced_report, mode, k + 1)
    else:
        decimal = int("".join(str(i) for i in sliced_report[:, 0]), 2)
    return decimal


oxygen_generator_rating = find_life_support_rating(transposed_report, "O2", 0)
CO2_scrubber_rating = find_life_support_rating(transposed_report, "CO2", 0)

print(f"Oxygen generator rating: {oxygen_generator_rating}, "
      f"CO2 scrubber rating: {CO2_scrubber_rating}, "
      f"life support rating: {oxygen_generator_rating*CO2_scrubber_rating}")

# endregion