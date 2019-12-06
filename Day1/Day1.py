mass = open('input1.txt', "r")  # when doing this, use m.readlines

# region --- Assignment 1 ---


def fuel(m):
    m = (m // 3) - 2
    if m <= 0:
        m = 0
    return (m)


fuel_req1 = 0

for i in mass.readlines():
    fuel_req1 += fuel(int(i))

print("Sum of the fuel requirements for modules:", fuel_req1)

# endregion

# region --- Assignment 2 ---


def extra_fuel(m):
    total_fuel = 0
    needed_fuel = m
    while needed_fuel > 0:
        needed_fuel = int(needed_fuel / 3) - 2
        if needed_fuel > 0:
            total_fuel += needed_fuel
    return total_fuel


mass = open('input1.txt', "r")  # when doing this, use m.readlines
fuel_req2 = 0
for i in mass.readlines():
    fuel_req2 += extra_fuel(int(i))

print("Sum of the fuel requirements for modules AND fuel:", fuel_req2)
