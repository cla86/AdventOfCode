#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    sequences = [list(map(int, line.strip().split(' '))) for line in f.readlines()]

def stepdown(lst):
    return [lst[i+1]-lst[i] for i in range(len(lst)-1)]

predictions = 0
rev_predictions = 0
for seq in sequences:
    stepdowns = [seq]
    seq = stepdown(seq)
    stepdowns.append(seq)
    while not all([x == 0 for x in seq]):
        seq = stepdown(seq)
        stepdowns.append(seq)
    
    # part 1
    for i in range(0, len(stepdowns))[::-1]:
        if i != 0:
            stepdowns[i-1].append(stepdowns[i-1][-1] + stepdowns[i][-1])
    predictions += stepdowns[0][-1]

    # part 2
    for i in range(0, len(stepdowns))[::-1]:
        if i != 0:
            stepdowns[i-1] = [stepdowns[i-1][0] - stepdowns[i][0]] + stepdowns[i-1]
    rev_predictions += stepdowns[0][0]

print(predictions)
print(rev_predictions)