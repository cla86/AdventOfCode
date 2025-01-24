#!/usr/bin/env python3
from collections import defaultdict

with open('input.txt.mini', 'r') as f:
    data = f.read().splitlines()

# part 1
points = []
for card in data:
    _, numbers = card.split(':')
    winning, owned = numbers.strip().lstrip().split('|')
    winning = list(map(int, winning.split()))
    owned = list(map(int, owned.split()))
    #break

    n = 0
    for i in owned:
        if i in winning:
            if n == 0:
                n += 1
            else:
                n *= 2
    points.append(n)

print(sum(points))    