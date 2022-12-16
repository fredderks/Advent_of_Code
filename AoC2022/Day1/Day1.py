calories_input = open('input.txt', "r").read().splitlines()

inventories = []
calories = 0
for food in calories_input:
    if food == '':
        inventories.append(calories)
        calories = 0
    else:
        calories += int(food)

print(max(inventories))

print(sum(sorted(inventories, reverse=True)[:3]))
