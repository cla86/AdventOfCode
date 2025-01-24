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

# part 2
scratchcards = [(card_number, 
                list(map(int, winning.split())),
                list(map(int, owned.split())))
                for card_number, numbers in enumerate(data, 1) for numbers in [numbers.split(':')]
                for winning, owned in [numbers[1].strip().lstrip().split('|')]]

copies = defaultdict(int)
for card_number, winning, owned in scratchcards:
    copies[card_number] += 1
    n = 0
    multiplier = copies[card_number] if card_number in copies.keys() else 1
    for number in owned:
        if number in winning: n += 1
    #print(n)
    if n > 0:
        for j in range(1, n  + 1):
            copies[card_number + j] +=  multiplier

print(sum(copies.values()))


            
