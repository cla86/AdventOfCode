#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    cosmos = [list(line.strip()) for line in f.readlines()]

def solve(cosmos, factor):
    def _empty(cosmos):
        rows = []
        cols = []

        for i, row in enumerate(cosmos):
            if '#' not in row:
                rows.append(i)

        transposed = [[cosmos[j][i] for j in range(len(cosmos))] for i in range(len(cosmos[0]))]

        for i, col in enumerate(transposed):
            if '#' not in col:
                cols.append(i)

        return rows, cols

    galaxies = [(i, j) for i, row in enumerate(cosmos) for j, cell in enumerate(row) if cell == '#']
    pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    
    empty_rows, empty_cols = _empty(cosmos)

    empty = factor - (1 if factor > 1 else 0)
    distance = 0
    for pair in pairs:
        x, y = pair
        distance += abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        r = sorted([x[0], y[0]])
        for row in empty_rows:
            if r[0] < row < r[1]:
                distance += empty

        c = sorted([x[1], y[1]])
        for col in empty_cols:
            if c[0] < col < c[1]:
                distance += empty
    
    return distance

# part 1
distance = solve(cosmos, 1)
print("Part 1:", distance)

# part 2
distance = solve(cosmos, 1000000)
print("Part 2:", distance)