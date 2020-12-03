import math
def read_reactions(file):
    input = open(file)
    output = {}
    for line in input.readlines():
        line = str(line)
        line = line.replace("\n", "")
        elements, product = line.split(' => ')
        prod_val, prod_name = product.split(" ")
        dict_values = [int(prod_val)]
        elements = elements.split(", ")
        for element in elements:
            el_val, el_name = element.split(" ")
            el_pair = [el_name, int(el_val)]
            dict_values.append(el_pair)
        output[prod_name] = dict_values
    return output


def sum_products(reactions_list, requirements, line):
    print("\n --- starting new calculation --- ")
    print(requirements)
    new_reaction_req = requirements.copy()                      # copy dictionary
    el_needed = []
    for i in reactions_list[line]:
        el_needed.append(i.split(" ")[1])
    print("elements needed:", el_needed)
    for element in el_needed:                              # for each element in the first requirement: 7 A, 1 E
        for product in reactions_list:                           # for each product (right side) in the reactions list
            # print("Elements not already calculated:", product , element, element not in dict)
            if element == product.split(" ")[1]:        # see if the element of the reaction is in the reactions list
                print("For element:", element)
                for sub_element in reactions_list[product]:      # for each sub_element of a matched reaction: for 1E: 7 A, 1 D
                    print("we need:", sub_element)
                    el_amount, el_name = sub_element.split(" ")
                    if el_name in requirements:
                        el_amount = str(int(el_amount) + int(requirements[el_name]))
                    new_reaction_req[el_name] = el_amount
    print(" - new_reaction_req - ")
    for i in new_reaction_req.items():
        print(i)
    return new_reaction_req

reactions = read_reactions("reactions1.txt")
for i in reactions.items():
    print(i)
print()


fuel_req = {}
reactions_req = {}
for element in reactions['FUEL'][1:]:
    fuel_req[element[0]] = element[1]*reactions['FUEL'][0]

print("Fuel req:",fuel_req)

for element in fuel_req:
    new_reaction_req = []
    if element != 'ORE':
        for sub_element in reactions[element][1:]:  # 'ORE', 9
            req_amount = math.ceil(fuel_req[element] / reactions[element][0])
            print(sub_element, 'req_amount', req_amount, reactions[element][0])
            el_amount = sub_element[1] * req_amount  # 9 * 10
            print(sub_element, el_amount)
            if sub_element[0] in reactions_req:
                el_amount = el_amount + reactions_req[sub_element[0]]
            reactions_req[sub_element[0]] = el_amount
fuel_req = reactions_req                        # {'A': 10, 'B': 23, 'C': 37}
print("Fuel req:",fuel_req)

reactions_req = {}
for element in fuel_req:                        # 'A': 10
    new_reaction_req = []
    if element != 'ORE':
        for sub_element in reactions[element][1:]:      # 'ORE', 9
            req_amount = math.ceil(fuel_req[element]/reactions[element][0])
            print(sub_element, 'req_amount', req_amount, reactions[element][0])
            el_amount = sub_element[1]*req_amount    # 9 * 10
            print(sub_element, el_amount)
            if sub_element[0] in reactions_req:
                el_amount = el_amount + reactions_req[sub_element[0]]
            reactions_req[sub_element[0]] = el_amount

fuel_req = reactions_req                        # {'A': 10, 'B': 23, 'C': 37}
print("Fuel req:",fuel_req)

reactions_req = {}
for element in fuel_req:                        # 'A': 10
    new_reaction_req = []
    if element != 'ORE':
        for sub_element in reactions[element][1:]:      # 'ORE', 9
            req_amount = math.ceil(fuel_req[element]/reactions[element][0])
            print(sub_element, 'req_amount', req_amount, reactions[element][0])
            el_amount = sub_element[1]*req_amount    # 9 * 10
            print(sub_element, el_amount)
            if sub_element[0] in reactions_req:
                el_amount = el_amount + reactions_req[sub_element[0]]
            reactions_req[sub_element[0]] = el_amount
print(reactions_req)



#
# fuel_req = {}
# reaction_req = {}
# for product in reactions:
#     if product == 'FUEL':
#         for element in reactions[product][1:]:
#             # print(element)
#             fuel_req[element[0]] = element[1]
#         print("FUEL_req:", fuel_req)
#     else:
#         print(product)
#         if product in fuel_req:
#             for element in reactions[product][1:]:
#                 # print(element)
#                 reaction_req[element[0]] = element[1]
#             print("reaction_req:", reaction_req)
#


# reaction_req = {}
# for product in reactions:
#     prod_amount, prod_name = product.split(" ")
#     if prod_name == 'FUEL':
#         for element in reactions[product]:
#             # print(element)
#             el_amount, el_name = element.split(" ")
#             reaction_req[el_name] = el_amount
# print("reactions_req:", reaction_req)

# print(" --- ")
# for i in reactions.keys(): # TODO Have not yet taken into account element can have amounts higher than 1
#     line = str(i)
#     reaction_req = sum_products(reactions, reaction_req, line)

# reaction_req = sum_products(reactions, reaction_req, -1)
# reaction_req = sum_products(reactions, reaction_req, -2)
# reaction_req = sum_products(reactions, reaction_req, -3)

# print(" --- new_reaction_req --- ")
# for i in new_reaction_req.items():
#     print(i)

