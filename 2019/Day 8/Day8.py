picture = open("picture.txt")
picture = str(picture.readlines()[0])

layer_size = 25 * 6
width = 25


# region --- Assignment 1 ---

def slice_into_layers(picture, layer_size):
    pos = 0
    layer_list = []
    for i in range(layer_size, len(picture) + 1, layer_size):  # Slice up the picture into layer sized pieces
        layer_list.append(picture[pos:i])
        pos = i
    return layer_list


layer_list = slice_into_layers(picture, layer_size)

zeroes = []
for layer in layer_list:  # Count number of zeroes in each layer
    zeroes.append(layer.count('0'))

index = zeroes.index(min(zeroes))  # Layer with least zeroes

target_layer = layer_list[index]
ones = target_layer.count('1')
twos = target_layer.count('2')
print('--- Assignment 1 ---\nLayer:', index, '- ones:', ones, '- twos:', twos, 'sum:', ones * twos)


# endregion

# region --- Assigment 2 ---

def listToString(s):
    # initialize an empty string
    str1 = ""
    # return string
    return str1.join(s)


layer_list = slice_into_layers(picture, layer_size)

final_layer = [2 for i in range(layer_size)]  # Initialize final layer

for layer in layer_list:  # Overwrite every 2 in top layer with 1 or 0 from
    # print("Current layer:", layer)                        # first underlying layer
    for char in range(layer_size):
        if int(layer[char]) < 2 and int(final_layer[char]) > 1:
            # print("Current char:", layer[char])
            final_layer[char], = layer[char]

final_layer = listToString(final_layer)

print('\n--- Assignment 2 ---')

start = 0
for i in range(0, layer_size + 1, width):
    print(final_layer[start:i])
    start = i

# endregion
