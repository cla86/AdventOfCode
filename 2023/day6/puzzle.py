#!/usr/bin/env python3
import re
from functools import reduce

with open('input.txt', 'r') as f:
    data = f.readlines()

times = list(map(int, re.findall(r'\d+', data[0])))
distances = list(map(int, re.findall(r'\d+', data[1])))
races = list(zip(times, distances))

# part 1
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

print(reduce(lambda x, y: x * y, possibilities))

