#!/usr/bin/env python3
import heapq

with open('input.txt', 'r') as f:
    maze = f.readlines()
    maze = [list(x.strip()) for x in maze]

#print(maze)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'E':
            stop = (i, j)

def solve(maze, start, stop):
    direction = (0, 1)
    queue = [(0, start, direction)]
    seen = set()

    while queue:
        cost, position, direction = heapq.heappop(queue)
        x, y = position
        dx, dy = direction
        
        if (x, y) == stop:
            return cost
        
        if (x, y, dx, dy) in seen:
            continue
        seen.add((x, y, dx, dy))

        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[nx][ny] != '#':
            heapq.heappush(queue, (cost + 1, (nx, ny), (dx, dy)))
        
        lx, ly = -dy, dx
        rx, ry = dy, -dx
        heapq.heappush(queue, (cost + 1000, (x, y), (lx, ly)))
        heapq.heappush(queue, (cost + 1000, (x, y), (rx, ry)))

# part 1
print(solve(maze, start, stop))