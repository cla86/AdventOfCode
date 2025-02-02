#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    platform = [x.strip() for x in f.readlines()]

def tilt(platform):
    sum = 0
    for row in list(zip(*platform)):
        l = len(row)
        for i in range(0, len(row)):
            if row[i] == 'O':
                for j in reversed(range(0, i)):
                    if row[j] == 'O':
                        l -= 1
                        break
                    elif row[j] == '#':
                        l = len(row) - 1 - j
                        break
                sum += l

    return sum

# part 1
print(tilt(platform))