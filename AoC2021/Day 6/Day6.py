import time
import numpy as np

input_ages = open('input.txt', "r").read().split(",")
input_ages = np.array([int(fish) for fish in input_ages])

# region --- Assignment 1 ---

simulation_duration = 18
for day in range(simulation_duration):
    input_ages -= 1
    newborns = [8 for fish in input_ages if fish == -1]
    input_ages = [6 if fish == -1 else fish for fish in input_ages]
    input_ages = np.append(input_ages, np.array(newborns, dtype=np.int32))

print(f"After {simulation_duration} days, there would be {len(input_ages)} lanternfish")

# endregion

# region --- Assignment 2 ---

tic = time.perf_counter()

simulation_duration = 256
for day in range(simulation_duration):
    tac1 = time.perf_counter()
    input_ages -= 1
    tac2 = time.perf_counter()
    newborns = [8 for fish in input_ages if fish == -1]
    tac3 = time.perf_counter()
    input_ages = [6 if fish == -1 else fish for fish in input_ages]
    tac4 = time.perf_counter()
    input_ages = np.append(input_ages, np.array(newborns, dtype=int))
    tac5 = time.perf_counter()
    print(f"After {day} days: {input_ages}")
    print(f"Time taken: {tac2-tac1:0.4f}, {tac3-tac2:0.4f}, {tac4-tac3:0.4f}, {tac5-tac4:0.4f}, total: {tac5-tac1:0.2f}")

toc = time.perf_counter()

print(f"After {simulation_duration} days, there would be {len(input_ages)} lanternfish")
print(f"Completed operation in {toc - tic:0.4f} seconds")

# endregion
