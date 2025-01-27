#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    instructions, nodes = f.read().split('\n\n')

instructions = list(instructions)
nodes = [[elem.strip(), lr.strip()] for elem, lr in [points.split('=') for points in nodes.split('\n')]]
nodes = {node[0]: [left.lstrip('('), right.lstrip().strip(')')] for node in nodes for left, right in [node[1].split(',')]}

i = 0
start = nodes['AAA']
end = nodes['ZZZ']

while True:
    for direction in instructions:
        if direction == "L": start = nodes[start[0]]
        if direction == "R": start = nodes[start[1]]

        i += 1
        if start == end:
            break

    if start == end:
        break
print(i)