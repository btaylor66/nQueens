#!/usr/bin/env python

import logging
import os
n=4

# Create object? n, board, ?

log = logging.getLogger(__name__)

def initialize_board(n):
	print("Creating board")
	board = [ [" "] * n for unused in range(n)]
	return board

def check_queen(x,y,board):
    n = len(board)
    count = 0
    print(board[x][y])
    for i in range(len(board)):
        if board[i][y] == "Q" and i != x:
            # print("X FAIL!!",i," ",y)
            board[i][y] = "X"
            count += 1
        if board[x][i] == "Q" and i !=y:
            # print("Y FAIL!!",x," ",i)
            board[x][i] = "X"
            count += 1

    # checking diagonal
    if x <= y:
        start_x = 0
        start_y = y - x
    else:
        start_x = x - y
        start_y = 0

    while start_x < n and start_y < n:
        if board[start_x][start_y] == "Q" and start_x != x:
            print("Diag FAIL 1 !!",start_x," ",start_y)
            board[start_x][start_y] = "X"
            count += 1
        start_x += 1
        start_y += 1

    if x <= y:
        start_x = x - ( n- y )
        start_y = n
    else:
        start_x = 0
        start_y = y + x

    while start_x < n and start_y >= 0 and start_y < n and x >= 0:
        if board[start_x][start_y] == "Q" and start_x != x:
            print("Diag FAIL 2!!",start_x," ",start_y)
            board[start_x][start_y] = "X"
            count += 1
        start_x += 1
        start_y -= 1
    if count == 0:
        print("Verified")
    else:
        print("Found ",count," misplaced queens")

def locate_queens(board):
    x = 0
    y = 0

    # Checking X and Y
    for row in board:
        for cell in row:
            if cell == "Q":
                print("Found One! X:",x," Y:",y)
                check_queen(x,y,board)
            y += 1
        y = 0
        x += 1

def print_board(board):
    for x in board:
        for y in x:
            print('|',y,'|',end='')
        print()

def  place_queen(x,y,board):
    board[x][y] = "Q"
    return board

def main():
    board_size = 4
    board = initialize_board(board_size)

    board = place_queen(0, 0, board)
    board = place_queen(3, 3, board)
    locate_queens(board)
    print_board(board)
    print()

    board = initialize_board(board_size)
    board = place_queen(0, 3, board)
    locate_queens(board)
    print_board(board)
    print()

    board = initialize_board(board_size)
    board = place_queen(3, 3, board)
    board = place_queen(3, 0, board)
    locate_queens(board)
    print_board(board)
    print()

    board = initialize_board(board_size)
    board = place_queen(0, 3, board)
    board = place_queen(3, 0, board)
    locate_queens(board)
    print_board(board)
    print()

    board = initialize_board(board_size)
    board = place_queen(1, 1, board)
    board = place_queen(3, 3, board)
    board = place_queen(0, 2, board)
    locate_queens(board)
    print_board(board)

    print()

    board = initialize_board(board_size)
    board = place_queen(0, 2, board)
    board = place_queen(1, 0, board)
    board = place_queen(2, 3, board)
    board = place_queen(3, 1, board)
    locate_queens(board)
    print_board(board)
if __name__ == '__main__':
	main()
