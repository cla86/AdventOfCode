#!/usr/bin/env python3
import re
from functools import reduce

with open('input.txt.mini', 'r') as f:
    data = f.readlines()

times = list(map(int, re.findall(r'\d+', data[0])))
distances = list(map(int, re.findall(r'\d+', data[1])))
races = list(zip(times, distances))

def solve(races):
    possibilities = []
    for time, distance in races:
        n = 0
        for charge in range(1, int(time)):
            speed = charge
            time_left = time - charge
            max_distance = speed * time_left

            if max_distance > distance:
                n += 1

        possibilities.append(n)
    return possibilities

# part 1
print(reduce(lambda x, y: x * y, solve(races)))

# part 2
races = [(int(''.join(map(str, times))), int(''.join(map(str, distances))))]
print(reduce(lambda x, y: x * y, solve(races)))
