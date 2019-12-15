def orbit_input(file):
    # Return test input in list form
    if file == "test":
        orbittest = [('COM', 'B'),
                     ('B', 'C'),
                     ('C', 'D'),
                     ('D', 'E'),
                     ('E', 'F'),
                     ('B', 'G'),
                     ('G', 'H'),
                     ('D', 'I'),
                     ('E', 'J'),
                     ('J', 'K'),
                     ('K', 'L')]
        return orbittest

    # Return actual input in list form
    elif file == "real":
        input = open('input.txt')
        orbit = []
        for line in input.readlines():
            line = str(line)
            line = line.replace("\n", "")
            line = (line[:3], line[4:])
            orbit.append(line)
        return orbit

    elif file == "santa":
        orbittest = [('COM', 'B'),
                     ('B', 'C'),
                     ('C', 'D'),
                     ('D', 'E'),
                     ('E', 'F'),
                     ('B', 'G'),
                     ('G', 'H'),
                     ('D', 'I'),
                     ('E', 'J'),
                     ('J', 'K'),
                     ('K', 'L'),
                     ('K', 'YOU'),
                     ('I', 'SAN')]
        return orbittest


# region --- Assignment 1 ---
# print('\n--- Assignment 1 ---')
# orbit = orbit_input("real")
#
# # create list of unique planets
# unique = []
# for pair in orbit:
#     for i in pair:
#         if i not in unique:
#             unique.append(i)
#
# # Create list of all planets on the right side of the divider
# set2 = []
# for pair in orbit:
#     set2.append(pair[1])
#
# # Find out which of the unique planets does not occur in on the right side of the divider, this is the origin
# origin = None
# for planet in unique:
#     if planet not in set2:
#         origin = planet
#         print("Origin:", origin)
#
# unique.remove(origin)
#
# print("Number of unique planets:", len(unique))
#
# # Find orbits
#
# total_orbits = 0
# planet_counter = 0
# for planet in unique:
#     i = planet
#     counter = 1
#     planet_counter += 1
#     lol = True
#     while lol:
#         for pair in orbit:
#             if pair[1] == i:
#                 if pair[0] == origin:
#                     # print(planet, 'orbits', pair[0], ' - ', counter, 'orbits\n')
#                     total_orbits += counter
#                     print(planet_counter, "-", total_orbits)
#                     lol = False
#                 else:
#                     # print(pair[1], 'orbits', pair[0])
#                     i = pair[0]
#                     counter += 1
#                     break
#
# print('\nTotal number of orbits:', total_orbits)

# endregion

# region --- Assignment 2 ---
print('\n--- Assignment 2 ---')

orbit = orbit_input("real")

origin = 'COM'
unique = ['YOU', 'SAN']

yourorbit = []
sanorbit = []

for planet in unique:
    i = planet
    counter = 1
    lol = True
    while lol:
        for pair in orbit:
            if pair[1] == i:
                if pair[0] == origin:
                    print(planet, 'orbits', pair[0], ' - ', counter, 'orbits\n')
                    lol = False
                else:
                    if planet == 'YOU':
                        yourorbit.append(pair[1])
                    elif planet == 'SAN':
                        sanorbit.append(pair[1])
                    i = pair[0]
                    counter += 1
                    break

print('YOU:', yourorbit)
print('SAN:', sanorbit)

yourdiff = list(set(yourorbit) - set(sanorbit))
sandiff = list(set(sanorbit) - set(yourorbit))
yourdiff.remove('YOU')
sandiff.remove('SAN')
print('\nNumber of transfers:', len(yourdiff) + len(sandiff))

# endregion
