# Part One

strategy_input = open('input.txt', "r").read()

replacements = [('A', '1'), ('X', '1'), ('B', '2'), ('Y', '2'), ('C', '3'), ('Z', '3')]
for char, replacement in replacements:
    if char in strategy_input:
        strategy_input = strategy_input.replace(char, replacement)

strategy_guide = []
for round in strategy_input.splitlines():
    strategy_guide.append(round.split(' '))

total_score = 0
for round in strategy_guide:
    elf = int(round[0])
    me = int(round[1])
    result = elf - me
    if result == -1 or result == 2:
        score = me + 6 # Win
    elif result == -2 or result == 1:
        score = me + 0 # Loss
    else:
        score = me + 3 # Draw
    total_score += score

print(total_score)

# Part Two


def play_round(elf, outcome):
    if outcome == 6: # Win
        if elf == 3:
            score = 1 + 6
        else:
            score = elf + 1 + 6
    elif outcome == 3: # Draw
        score = elf + 3
    else: # Lose
        if elf == 1:
            score = 3
        else:
            score = elf - 1
    return score


strategy_input = open('input.txt', "r").read()
replacements = [('A', '1'), ('X', '0'), ('B', '2'), ('Y', '3'), ('C', '3'), ('Z', '6')]
for char, replacement in replacements:
    if char in strategy_input:
        strategy_input = strategy_input.replace(char, replacement)

strategy_guide = []
for round in strategy_input.splitlines():
    strategy_guide.append(round.split(' '))

total_score = 0
for round in strategy_guide:
    elf = int(round[0])
    outcome = int(round[1])
    score = play_round(elf, outcome)
    # print(score)
    total_score += score

print(total_score)
