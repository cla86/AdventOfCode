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


composable = []
for pattern in desired:
    res = valid_design(0, pattern, available)
    composable.append(res)

# part 1
print(sum(composable))