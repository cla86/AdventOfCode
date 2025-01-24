#!/usr/bin/env python3

with open("input.txt.mini") as f:
    t_available, t_desired = f.read().split("\n\n")
    available = t_available.split(", ")
    desired = t_desired.split("\n")

def valid_design(position, pattern, available):
    if position == len(pattern):
        return 1
    
    for design in available:
        next_position = position + len(design)
        if next_position <= len(pattern) and pattern[position:next_position] == design:
            if valid_design(next_position, pattern, available):
                return 1
    return 0

# part 1
composable = []
for pattern in desired:
    res = valid_design(0, pattern, available)
    composable.append(res)

print(sum(composable))

# part 2
def valid_ways(position, pattern):
  if position >= len(pattern):
    return 1
  
  ways = 0
  for towel in available:
    next_pos = position + len(towel)
    if pattern[position:next_pos] == towel:
      ways += valid_ways(next_pos, pattern)
  return ways

combinations = 0
for pattern in desired:
  combinations += valid_ways(0, pattern)

print(combinations)