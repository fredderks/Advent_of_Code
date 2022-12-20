def crate_mover_9000(stacks, procedure):
    quantity, origin, destination = map(int, procedure.split(' ')[1:6:2])
    origin -= 1
    destination -= 1
    stacks[destination] = stacks[origin][:quantity][::-1] + stacks[destination]
    stacks[origin] = stacks[origin][quantity:]


def crate_mover_9001(stacks, procedure):
    quantity, origin, destination = map(int, procedure.split(' ')[1:6:2])
    origin -= 1
    destination -= 1
    stacks[destination] = stacks[origin][:quantity] + stacks[destination]
    stacks[origin] = stacks[origin][quantity:]


# Part One
procedure_input = open('input.txt', "r").read().splitlines()
stacks = open('input_stacks.txt', 'r').read().splitlines()

for procedure in procedure_input:
    crate_mover_9000(stacks, procedure)

print("".join([x[0] for x in stacks]))

# Part Two
stacks = open('input_stacks.txt', 'r').read().splitlines()

for procedure in procedure_input:
    crate_mover_9001(stacks, procedure)

print("".join([x[0] for x in stacks]))
