#!/usr/bin/env python3

with open('input.txt') as f:
    data = f.readlines()

for i in data:
    print(i.strip().replace('',' '))

board = [list(map(int, (s.strip()))) for s in data]

def on_board(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

starts = set()
m = len(board)
n = len(board[0])
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            starts.add((i, j))

def walk(x, y, seen, part2=False):
    if board[x][y] == 9 and not part2: # and (x, y) not in seen:
        seen.add((x, y))
    if board[x][y] == 9 and part2:
        seen += 1
        return seen

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dir in directions:
        dir_x, dir_y = x + dir[0], y + dir[1]

        if on_board(dir_x, dir_y, m, n) and board[dir_x][dir_y] == board[x][y] + 1:
            if not part2:
                walk(dir_x, dir_y, seen)
            else:
                seen = walk(dir_x, dir_y, seen, part2=True)
                #return seen

    ##print(seen)
    if not part2:
        return len(seen)
    else:
        return seen

# part 1
print("Starts:", starts)
print(list(walk(x, y, set()) for (x, y) in starts))
print(sum(walk(x, y, set()) for (x, y) in starts))

# part 2
seen = 0
for x, y in starts:
    seen = walk(x, y, seen, part2=True) # for (x, y) in starts)
print(seen)