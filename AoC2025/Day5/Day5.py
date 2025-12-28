fresh_ID_ranges_input, available_IDs_input = open('testinput.txt', "r").read().split("\n\n")

fresh_ID_ranges = [[int(ID_range.split('-')[0]),int(ID_range.split('-')[1])] for ID_range in fresh_ID_ranges_input.splitlines()]
# available_IDs = list(map(int, available_IDs_input.splitlines()))


def sum_ranges(ranges):
    ranges = list(set(tuple(lst) for lst in ranges))
    ranges.sort(key=lambda cur_range: cur_range[0])

    total_sum = 0
    cur_start, cur_end = ranges[0]

    for compared_range in ranges[1:]:
        if compared_range[0] <= cur_end:  # overlap
            print([cur_start,cur_end], compared_range, 'overlap found, updating to', [cur_start, max(cur_end, compared_range[1])])
            cur_end = max(cur_end, compared_range[1])
        else: # no overlap
            total_sum += cur_end - cur_start + 1
            cur_start, cur_end = compared_range

    total_sum += cur_end - cur_start + 1
    return total_sum


sum_ranges = sum_ranges(fresh_ID_ranges)
print(sum_ranges)
