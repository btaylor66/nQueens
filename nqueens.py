#!/usr/bin/env python

import logging

class Board:

    def __init__(self,n):
        self.n = n     # Size of board and number of queens to be placed
        self.board = [ [" "] * n for unused in range(n)]

    def print_board(self):
        for x in self.board:
            for y in x:
                print('|', y, '|', end='')
            print()

    def place_queen(self,x,y):
        try:
            self.board[x][y] = "Q"
        except IndexError as err:
            print("Error placing queen in ",x,",",y," : ", err)
    def check_queen(self, x, y):

        count = 0

        for i in range(self.n):
            if self.board[i][y] == "Q" and i != x:
                # print("X FAIL!!",i," ",y)
                self.board[i][y] = "X"
                count += 1
            if self.board[x][i] == "Q" and i != y:
                # print("Y FAIL!!",x," ",i)
                self.board[x][i] = "X"
                count += 1

        # checking diagonal
        if x <= y:
            start_x = 0
            start_y = y - x
        else:
            start_x = x - y
            start_y = 0

        while start_x < self.n and start_y < self.n:
            if self.board[start_x][start_y] == "Q" and start_x != x:
                #print("Diag FAIL 1 !!", start_x, " ", start_y)
                self.board[start_x][start_y] = "X"
                count += 1
            start_x += 1
            start_y += 1

        if x <= y:
            start_x = x - (self.n - y)
            start_y = self.n
        else:
            start_x = 0
            start_y = y + x

        while start_x < self.n and start_y >= 0 and start_y < self.n and x >= 0:
            if self.board[start_x][start_y] == "Q" and start_x != x:
                print("Diag FAIL 2!!", start_x, " ", start_y)
                self.board[start_x][start_y] = "X"
                count += 1
            start_x += 1
            start_y -= 1
        if count == 0:
            # print("Verified")
            return 0
        else:
            # print("Found ",count," misplaced queens")
            return count

    def verify_board(self):
        x = 0
        y = 0
        queens_failed = 0

        # Checking X and Y
        for row in self.board:
            for cell in row:
                if cell == "Q":
                    # print("Found One! X:",x," Y:",y)
                    queens_failed += self.check_queen(x,y)
                y += 1
            y = 0
            x += 1
        # if queens_failed == 0:
        #    print("Verified")
        #else:
        #    print(queens_failed, "Queens misplaced")

        return queens_failed



log = logging.getLogger(__name__)






def main():

    size4 = Board(4)
    size4.place_queen(0, 0)
    size4.place_queen(0, 5)
    size4.verify_board()
    print()
    size5 = Board(4)
    size5.place_queen(3, 0)
    size5.place_queen(3, 3)
    size5.print_board()
    size5.verify_board()
    size5.print_board()

if __name__ == '__main__':
	main()
