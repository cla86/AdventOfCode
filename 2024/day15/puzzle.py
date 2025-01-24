#!/usr/bin/env python3
# https://adventofcode.com/2024/day/15

import os
import time

with open('input.txt', 'r') as f:
    warehouse, moves = f.read().split('\n\n')

moves = list(moves.replace('\n', ''))
board = [[y for y in list(x)] for x in warehouse.split('\n')]


for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '@':
            starting_pos = (i, j)

def print_board(board, direction):
    os.system('clear')
    for i in board:
        print("    ", end='')
        for j in i:
            print(j, end='')
        print("  ", direction, end='\n')
    print(direction)
    time.sleep(0.15)

directions = { 'v': (1, 0),
              '>': (0, 1),
              '<': (0, -1),
              '^': (-1, 0)
            }

# part 1
for move in moves:
    x, y = starting_pos
    dir_x, dir_y = directions[move]
    next_pos = (x + dir_x, y + dir_y)
    if board[next_pos[0]][next_pos[1]] == '#':
        continue
    if board[next_pos[0]][next_pos[1]] == '.':
        board[next_pos[0]][next_pos[1]] = '@'
        board[x][y] = '.'
        starting_pos = next_pos
        #print_board(board, move)
        continue

    to_move = next_pos
    while board[to_move[0]][to_move[1]] == 'O':
        to_move = (to_move[0] + dir_x, to_move[1] + dir_y)
    if board[to_move[0]][to_move[1]] == '#':
        continue
    board[x][y] = '.'
    board[to_move[0]][to_move[1]] = 'O'
    board[next_pos[0]][next_pos[1]] = '@'
    starting_pos = next_pos
    #print_board(board, move)

#print_board(board, move)

gps = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'O':
            gps += (100 * i) + j

print(gps)