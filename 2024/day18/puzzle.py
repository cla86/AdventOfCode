#!/usr/bin/env python3
# https://adventofcode.com/2024/day/18

from collections import deque

with open("input.txt.mini") as f:
    lines = f.read().splitlines()

size = 6
corrupted = 12

def create_board(size):
    return [["." for _ in range(size + 1)] for _ in range(size + 1)]

grid = create_board(size)

i = 0
for line in lines:
    x, y = line.split(",")
    grid[int(y)][int(x)] = "#"
    i += 1
    if i == corrupted:
        break

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
rows, cols = len(grid), len(grid[0])

def bfs(grid, start, end):
    x, y = start
    queue = deque()
    queue.append(((x, y), 0))
    seen = set()    

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == end:
            return dist
        seen.add((x, y))
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "." and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

def print_board(grid):
    for row in grid:
        print("".join(row))

# part 1
start, end = (0, 0), (size, size)
res = bfs(grid, start, end)
print(res)

# part 2
grid = create_board(size)
for line in lines:
    x, y = line.split(",")
    grid[int(y)][int(x)] = "#"
    res = bfs(grid, start, end)

    if res is None:
        print(line)
        break


