# load the wire input into arrays for processing
def read_input(file):
    input = open(file, "r")
    wire = input.read()  # reads the file into a variable as one long string
    wire = wire.split(",")  # turns the string into an array of smaller strings
    input.close()
    return wire


def get_coords(path):
    wirecoords = []
    wirex = 0
    wirey = 0
    for i in path:
        direc = i[0]
        dist = int(i[1:4])
        for i in range(dist):
            if direc == "U":
                wirey += 1
            elif direc == "D":
                wirey -= 1
            elif direc == "R":
                wirex += 1
            elif direc == "L":
                wirex -= 1
            coords = (wirex, wirey)
            wirecoords.append(coords)
    return wirecoords


wire1 = read_input("input5.txt")
wire2 = read_input("input6.txt")

coords1 = get_coords(wire1)
coords2 = get_coords(wire2)

lowdist = 999999999999

for wire1 in coords1:
    for wire2 in coords2:
        if wire1 == wire2:
            print("Intersection at:", wire1)
            dist = abs(int(wire1[0])) + abs(int(wire1[1]))  # get the distance and compare to the current low
            print("At a distance of:", dist)
            if dist < lowdist:
                lowdist = dist
print("The closest intersection is at a distance of:", lowdist)