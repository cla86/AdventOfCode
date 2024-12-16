#!/usr/bin/env python3
#
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = list(map(int, f.read().split(' ')))

stones = defaultdict(int)
for stone in data:
    stones[stone] = 1

def removeLeadingZeros(num):
    for i in range(len(num)):
        if num[i] != '0':
            res = num[i::]
            return res
    return "0"

number_of_blinks = 25

def blink(part, number_of_blinks):
    stones = defaultdict(int)
    for stone in data:
        stones[stone] = 1

    for blink in range(1, number_of_blinks + 1):
        blinking = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                blinking[1] += count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                splited = (map(int, (str(stone)[:half],
                                        removeLeadingZeros(str(stone)[-half:]))))
                for k in splited:
                    blinking[k] += count
            else:
                v = stone * 2024
                blinking[v] += count
            stones = blinking

    print("Part", part + ":", sum(stones.values()))
    #print("type(stones)", type(stones))
    #print("len(stones.items())", len(stones.items()))

# part 1
blink("1", 25)

# part 2
blink("2", 75)
