

def decode_boarding_pass(binary_code):
    bin_row = binary_code[:7]
    bin_col = binary_code[7:]

    bin_row = bin_row.replace("F", "0")
    bin_row = bin_row.replace("B", "1")

    bin_col = bin_col.replace("L", "0")
    bin_col = bin_col.replace("R", "1")
    row = int(bin_row, 2)
    col = int(bin_col, 2)
    pass_id = row * 8 + col
    return [row, col, pass_id]


boarding_passes_bin = open('input.txt', "r").read().split()

# region --- Assignment 1 ---

decoded_passes = [decode_boarding_pass(boarding_pass)[2] for boarding_pass in boarding_passes_bin]

print("highest ID:", max(decoded_passes))

# endregion

# region --- Assignment 2 ---

pass_set = set(decoded_passes)
compare_set = set(range(min(decoded_passes), max(decoded_passes) + 1))
my_seat = compare_set - pass_set
print("my seat:", my_seat)

# endregion
