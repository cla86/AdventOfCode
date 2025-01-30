#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    cosmos = [list(line.strip()) for line in f.readlines()]

def expand(cosmos):
    w = len(cosmos[0])
    rows = []
    for i, row in enumerate(cosmos):
        if '#' not in row:
            rows.append(i)
    for row in reversed(rows):
        cosmos.insert(row, list('.' * w))

    transposed = [[cosmos[j][i] for j in range(len(cosmos))] for i in range(len(cosmos[0]))]

    h = len(transposed[0])
    cols = []
    for i, col in enumerate(transposed):
        if '#' not in col:
            cols.append(i)
    for col in reversed(cols):
        transposed.insert(col, list('.' * h))
    
    return [[transposed[j][i] for j in range(len(transposed))] for i in range(len(transposed[0]))]


cosmos = expand(cosmos)
galaxies = [(i, j) for i, row in enumerate(cosmos) for j, cell in enumerate(row) if cell == '#']

# part 1
pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
print(sum([abs(x[0] - y[0]) + abs(x[1] - y[1]) for x, y in pairs]))