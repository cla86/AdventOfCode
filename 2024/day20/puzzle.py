#!/usr/bin/env python3
import heapq

with open('input.txt', 'r') as f:
    maze = f.readlines()
    maze = [list(x.strip()) for x in maze]

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S': start = (i, j)
        if maze[i][j] == 'E': stop = (i, j)

def cheat(grid):
    cheat_candidates = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == '#':
                neighbors = []
                for dx, dy in directions:
                    if grid[i + dx][j + dy] in ['.', 'S', 'E']:
                        neighbors.append((dx, dy))
                if len(neighbors) > 1:
                    cheat_candidates.append((i, j))

    return cheat_candidates

def solve(maze, start, stop):
    path = [start]
    seen = set()
    steps = {}
    steps[start] = 0
    queue = [(0, start, path, steps)]

    while queue:
        cost, position, path, steps = heapq.heappop(queue)
        steps[position] = cost

        if position == stop:
            return cost, path, steps
        seen.add(position)

        x, y = position
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if maze[nx][ny] != '#' and (nx, ny) not in seen:
                heapq.heappush(queue, (cost + 1, (nx, ny), path + [(nx, ny)], steps))

cost, path, steps = solve(maze, start, stop)

# part 1
cheats = cheat(maze)
diffs = []
for cx, cy in cheats:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if (nx, ny) in steps.keys():
            neighbors.append(steps[(nx, ny)])
    diffs.append(abs(max(neighbors)-min(neighbors)-2))

print(len([x for x in diffs if x >= 100]))
