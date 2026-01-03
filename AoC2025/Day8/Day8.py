import math

input_list = open('input.txt', "r").read().splitlines()
junction_boxes = [tuple(map(int, item.split(','))) for item in input_list]


def euclid_dist(p, q):
    p1, p2, p3 = p
    q1, q2, q3 = q
    d = math.sqrt((p1 - q1) ** 2 + (p2 - q2) ** 2 + (p3 - q3) **2)
    return d


total_connections = []
number_junction_boxes = len(junction_boxes)

for i in range(number_junction_boxes):
    for j in range(i + 1, number_junction_boxes):
        box_a = junction_boxes[i]
        box_b = junction_boxes[j]
        total_connections.append((box_a, box_b, euclid_dist(box_a, box_b)))


total_connections.sort(key = lambda i: i[2])
total_connections = total_connections[:1000]  # Disable this line for part 2 #
total_connections = list(item[:2] for item in total_connections)

circuits = []
for box_a, box_b in total_connections:
    skip = False
    found = []
    for circuit in circuits:
        if box_a in circuit and box_b in circuit:
            skip = True
            break
        elif box_a in circuit:
            found.append((circuit, box_b))
        elif box_b in circuit:
            found.append((circuit, box_a))

    if skip:
        continue

    if len(found) == 1:
        circuit, point = found[0]
        circuit.append(point)
    elif len(found) == 2:
        circuit_1, _ = found[0]
        circuit_2, _ = found[1]
        circuit_1.extend(circuit_2)
        circuits.remove(circuit_2)
    else:
        circuits.append([box_a, box_b])

    if len(circuits[0]) == len(junction_boxes):
        print('Part 2 answer:', box_a[0] * box_b[0])
        break

circuits.sort(key=len, reverse=True)

size = 1
for i in circuits[:3]:
    size *= len(i)

print('Part 1 answer:', size)
