#!/usr/bin/env python3

with open('input.txt.mini', 'r') as f:
    data = f.readlines()
    grid = [list(x.strip()) + ['.'] for x in data]

pns = []

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

pns = []
total = 0
for x, row in enumerate(grid):
    neigbours = [] #set()
    part_number = ''
    #row.append('.')
    for y, char in enumerate(row):
        #print(y, len(row))
        if char.isdigit():
            part_number += char
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(row):
                    neigbours.append((nx, ny))
        else:
            for i, j in neigbours:
                #print((x, y), i, j)
                if grid[i][j] != '.' and not grid[i][j].isdigit():
                    pns.append(part_number)
                    total += int(part_number)
                    break
            neigbours = [] #set()
            part_number = ''

#print(pns)
#print(sum(list(map(int, pns))))
print(total)