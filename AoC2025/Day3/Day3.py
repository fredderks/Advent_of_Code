battery_banks = open('input.txt', "r").read().splitlines()

batteries_to_turn_on = 2

total_joltage = 0
for battery_bank in battery_banks:
    print(battery_bank)
    combined_batteries = ''
    last_battery = ''
    last_index = 0
    for i in range(batteries_to_turn_on - 1, -1, -1):
        current_index = battery_bank[last_index:].index(last_battery) + 1 + last_index if last_battery != '' else 0
        current_section = battery_bank[current_index:-i] if i > 0 else battery_bank[current_index:]
        current_max = str(max(current_section))
        combined_batteries = combined_batteries + current_max

        last_battery = current_max
        last_index = current_index
    print('combined:', combined_batteries)
    total_joltage += int(combined_batteries)

print(total_joltage)
