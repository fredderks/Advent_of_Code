import numpy as np

input_positions = open('input.txt', "r").read().split(",")
input_positions = [int(crab) for crab in input_positions]

# region --- Assignment 1 ---

fuel_dict = {}
for i in range(max(input_positions)):
    fuel_costs = [abs(crab-i) for crab in input_positions]
    fuel_dict[i] = sum(fuel_costs)

best_pos = min(fuel_dict, key=fuel_dict.get)
print(f"Move to {best_pos}, it only costs: {fuel_dict[best_pos]}")

# endregion

# region --- Assignment 2 ---

fuel_dict = {}
for i in range(max(input_positions)):
    fuel_costs = [(abs(crab-i)*(abs(crab-i)+1))//2 for crab in input_positions]
    fuel_dict[i] = sum(fuel_costs)

best_pos = min(fuel_dict, key=fuel_dict.get)
print(f"Move to {best_pos}, it only costs: {fuel_dict[best_pos]}")

# endregion
