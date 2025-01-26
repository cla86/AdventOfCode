#!/usr/bin/env python3
from collections import Counter

with open("input.txt", 'r') as f:
    data = [line.strip().split() for line in f]

rank = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

def classify(cards):
    counter = Counter(cards)
    most_common = counter.most_common()
    if most_common[0][1] == 5:
        return 7
    if most_common[0][1] == 4:
        return 6
    if most_common[0][1] == 3:
        if most_common[1][1] == 2:
            return 5
        return 4
    if most_common[0][1] == 2:
        if most_common[1][1] == 2:
            return 3
        return 2
    if most_common[0][1] == 1:
        return 1
    return 0

def score(cards):
    return [int(card) if card.isdigit() else rank[card] for card in cards]

# part 1
scored = sorted([[cards, classify(cards), score(cards), bid] for cards, bid in data], key=lambda x: (x[1], x[2]))
total_winnings = 0
for i, scores in enumerate(scored, 1):
    total_winnings += i * int(scores[3])

print(total_winnings)