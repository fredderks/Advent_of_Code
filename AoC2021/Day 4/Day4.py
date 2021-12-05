import numpy as np


def input_to_bingo_cards(input):
    bingo_cards = []
    bingo_card = []
    for line in input:
        if line != "":
            bingo_row = [number for number in line.split()]
            bingo_card.append(bingo_row)
        else:
            bingo_cards.append(np.array(bingo_card))
            bingo_card = []
    bingo_cards.append(np.array(bingo_card))
    return bingo_cards


def bingo_round(card, number):
    card = np.where(card == str(number), 'X', card)
    for row in card:
        if np.all(row == 'X'):
            # print(f"BINGO, number: {number}")
            # print(card)
            return card, True
        else:
            continue
    transposed_card = card.transpose()
    for column in transposed_card:
        if np.all(column == 'X'):
            # print(f"BINGO, number: {number}")
            # print(card)
            return card, True
        else:
            continue
    return card, False


bingo_input = open('input.txt', "r").read().splitlines()
bingo_numbers = [int(number) for number in bingo_input[0].split(",")]
bingo_cards = input_to_bingo_cards(bingo_input[2:])

# region --- Assignment 1 ---

bingo_at_round = {}
solved_bingo_cards = []
for card_index in range(len(bingo_cards)):
    i = 1
    card = bingo_cards[card_index]
    for number in bingo_numbers:
        card = bingo_round(card, number)[0]
        if bingo_round(card, number)[1]:
            solved_bingo_cards.append([bingo_round(card, number)[0], number])
            bingo_at_round["card "+str(card_index)] = i
            break
        i += 1

winning_card = solved_bingo_cards[int(min(bingo_at_round, key=bingo_at_round.get).split()[1])]
remaining_sum = sum([int(number) for row in winning_card[0] for number in row if number != 'X'])

print("Winning card:")
print(winning_card[0])
print(f"{remaining_sum} * {winning_card[1]} = {remaining_sum * winning_card[1]}")

# endregion

# region --- Assignment 1 ---

bingo_at_round = {}
solved_bingo_cards = []
for card_index in range(len(bingo_cards)):
    i = 1
    card = bingo_cards[card_index]
    for number in bingo_numbers:
        card = bingo_round(card, number)[0]
        if bingo_round(card, number)[1]:
            solved_bingo_cards.append([bingo_round(card, number)[0], number])
            bingo_at_round["card "+str(card_index)] = i
            break
        i += 1

losing_card = solved_bingo_cards[int(max(bingo_at_round, key=bingo_at_round.get).split()[1])]
remaining_sum = sum([int(number) for row in losing_card[0] for number in row if number != 'X'])

print("Losing card:")
print(losing_card[0])
print(f"{remaining_sum} * {losing_card[1]} = {remaining_sum * losing_card[1]}")

# endregion
