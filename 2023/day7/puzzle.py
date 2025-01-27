#!/usr/bin/env python3
from collections import Counter

with open("input.txt", 'r') as f:
    data = [line.strip().split() for line in f]

def joker(counter, cards):
    jokers = counter['J']
    del counter['J']
    if jokers == 0:
        return classify(cards)
    if jokers == 5:
        return classify(cards.replace('J', 'A'))
    else:
        return classify(cards.replace('J', counter.most_common()[0][0]))

def classify(cards, wildcard=False):
    counter = Counter(cards)

    if wildcard:
        return joker(counter, cards)
    
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

def score(cards, wildcard=False):
    rank = {
        'T': 10,
        'J': 1 if wildcard else 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    return [int(card) if card.isdigit() else rank[card] for card in cards]

# part 1
scored = sorted([[cards, classify(cards), score(cards), bid] for cards, bid in data], key=lambda x: (x[1], x[2]))
total_winnings = 0
for i, scores in enumerate(scored, 1):
    total_winnings += i * int(scores[3])

print(total_winnings)

# part 2
scored = sorted([[cards, classify(cards, wildcard=True), score(cards, wildcard=True), bid] for cards, bid in data], key=lambda x: (x[1], x[2]))
total_winnings = 0
for i, scores in enumerate(scored, 1):
    total_winnings += i * int(scores[3])

print(total_winnings)