import textwrap
ID_ranges = open('input.txt', "r").read().split(",")

ID_sum = 0

for ID_range in ID_ranges:
    range_start_str, range_end_str = ID_range.split('-')
    range_start = int(range_start_str)
    range_end = int(range_end_str)
    for ID in range(range_start, range_end+1):
        ID_len = len(str(ID))

        # Part one
        # if ID_len % 2 == 0:
        #     half_len = int(ID_len/2)
        #     ID_first_half = int(str(ID)[half_len:])
        #     ID_last_half = int(str(ID)[:half_len])
        #     if ID_first_half == ID_last_half:
        #         ID_sum += ID

        # Part two
        valid_divisors = []
        for divisor in range(1, int(ID_len / 2) + 1):
            if ID_len % divisor == 0:
                valid_divisors.append(divisor)
        for divisor in valid_divisors:
            parts = textwrap.wrap(str(ID), divisor)
            if len(parts) > 1 and all(part == parts[0] for part in parts):
                ID_sum += ID
                break

print(ID_sum)
