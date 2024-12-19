#!/usr/bin/env python3
import re

with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [x.strip('\n') for x in data]

width = 101
height = 103
q1, q2, q3, q4 = 0, 0, 0, 0
robots = []

position_p = r"p=(\d+),(\d+)"
velocity_p = r"v=(-?\d+),(-?\d+)"
for robot in data:
    x, y = map(int, re.search(position_p, robot).groups())
    v_x, v_y = map(int, re.search(velocity_p, robot).groups())
    robots.append(((x, y), (v_x, v_y)))

    pos_x = (x + 100 * (v_x + width)) % width
    pos_y = (y + 100 * (v_y + height)) % height

    if pos_x < width // 2 and pos_y < height // 2:
        q1 += 1
    if pos_x > width // 2 and pos_y < height // 2:
        q2 += 1
    if pos_x < width // 2 and pos_y > height // 2:
        q3 += 1
    if pos_x > width // 2 and pos_y > height // 2:
        q4 += 1

# part 1
print(q1 * q2 * q3 * q4)

