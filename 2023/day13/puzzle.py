#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    patterns = f.read().split('\n\n')


def find_symmetry(pattern):
    rows, cols = len(pattern), len(pattern[0])
    for line in range(1, cols):  
        left, right = line - 1, line
        is_symmetric = True

        while left >= 0 and right < cols:
            for row in range(rows):
                if pattern[row][left] != pattern[row][right]:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
            left -= 1
            right += 1

        if is_symmetric:
            return line
    return None

sum = 0
for pattern in patterns:
    pattern = [list(x) for x in pattern.split('\n')]
    res = find_symmetry(pattern)
    if res != None:
        sum += res
        continue

    transposed = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
    res = find_symmetry(transposed)
    sum += res * 100

print(sum)
