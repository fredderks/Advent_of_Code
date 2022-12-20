section_assignments = open('input.txt', "r").read().splitlines()


def pair_contains(pair1, pair2):
    if (pair1[0] <= pair2[0] and pair1[1] >= pair2[1]) or (pair2[0] <= pair1[0] and pair2[1] >= pair1[1]):
        return 1
    else:
        return 0


def pair_overlaps(pair1, pair2):
    if pair1[1] >= pair2[0] and not pair1[0] > pair2[1]:
        return 1
    else:
        return 0


fully_containing_pairs = 0
for pair in section_assignments:
    elf1, elf2 = pair.split(",")
    elf1_pair = list(map(int, elf1.split('-')))
    elf2_pair = list(map(int, elf2.split('-')))
    fully_containing_pairs += pair_contains(elf1_pair, elf2_pair)

print(fully_containing_pairs)


overlapping_pairs = 0
for pair in section_assignments:
    elf1, elf2 = pair.split(",")
    elf1_pair = list(map(int, elf1.split('-')))
    elf2_pair = list(map(int, elf2.split('-')))
    overlapping_pairs += pair_overlaps(elf1_pair, elf2_pair)

print(overlapping_pairs)
