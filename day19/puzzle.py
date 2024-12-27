#!/usr/bin/env python3

with open("input.txt.mini") as f:
    t_available, t_desired = f.read().split("\n\n")
    available = t_available.split(", ")
    desired = t_desired.split("\n")

def can_compose(pattern, available):
    while pattern:
        match_found = False
        for element in sorted(available, key=len, reverse=True):
            if pattern.startswith(element):
                pattern = pattern[len(element):]
                match_found = True
                break
        if not match_found:
            return 0
    return 1

composable = []
for pattern in desired:
    composable.append(can_compose(pattern, available))
print(sum(composable))