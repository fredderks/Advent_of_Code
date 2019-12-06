# load the wire input into arrays for processing
def read_input(file):
    file = open(file, "r")
    wire = file.read()  # reads the file into a variable as one long string
    wire = wire.split(",")  # turns the string into an array of smaller strings
    file.close()
    return wire


def get_coords(path):
    wire_coordinates = []
    wire_x = 0
    wire_y = 0
    for i in path:
        direction = i[0]
        distance = int(i[1:])
        for i in range(distance):
            if direction == "U":
                wire_y += 1
            elif direction == "D":
                wire_y -= 1
            elif direction == "R":
                wire_x += 1
            elif direction == "L":
                wire_x -= 1
            coordinates = (wire_x, wire_y)
            wire_coordinates.append(coordinates)
    return wire_coordinates


wire1 = read_input("input5.txt")
wire2 = read_input("input6.txt")

coords1 = get_coords(wire1)
coords2 = get_coords(wire2)

intersect = set(coords1).intersection(coords2)
intersect = list(intersect)

print("Found", len(intersect), "intersections.")

# region --- Assignment 1 ---
minimum = 9999999999
for i in intersect:
    dist = abs(i[0]) + abs(i[1])
    if dist < minimum:
        minimum = dist
print("The closest intersection is at a Manhattan distance of:", minimum)
# endregion

# region --- Assignment 2 ---
intersect_steps = []
for i in intersect:
    intersect_steps.append((coords1.index(i) + 1) + (coords2.index(i) + 1))
print("The least number of steps to an intersection is:", min(intersect_steps))
# endregion
