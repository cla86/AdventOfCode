#!/usr/bin/env python3

with open('input.txt.mini', 'r') as f:
    data = f.readlines()

consts = {'red': 12,
          'green': 13,
          'blue': 14
          }

# part 1
possible = []
for line in data:
    game, rounds = line.strip('\n').split(':')
    sets = rounds.lstrip().split(';')
    sets = [s.split(',') for s in sets]
    game = int(game.split(' ')[1])
    invalid = False
    for s in sets:
        for cube in s:
            count, color = cube.lstrip().split(' ')
            if int(count) > consts[color]:
                invalid = True
                break

    if not invalid:
        possible.append(game)

print(sum(possible))

# part 2
import math
power = []
for line in data:
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    game, rounds = line.strip('\n').split(':')
    sets = rounds.lstrip().split(';')
    sets = [s.split(',') for s in sets]
    game = int(game.split(' ')[1])

    for s in sets:
        for cube in s:
            count, color = cube.lstrip().split(' ')
            if int(count) > mins[color]:
                mins[color] = int(count)
    m = math.prod(mins.values())
    power.append(m)
print(sum(power))

