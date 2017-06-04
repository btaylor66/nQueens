#!/usr/bin/env python

import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

class Board:

    def __init__(self,n):
        self.n = n     # Size of board and number of queens to be placed
        self.count = 0 # Number of queens placed
        self.board = [ ["_"] * n for unused in range(n)]
        self.solutions = {}

    def print_board(self):
        for x in self.board:
            for y in x:
                #print('|', y, '|', end='')
                print(y," ", end='')
            print()

    def place_queen(self,x,y):
        logging.debug("place_queen %i,%i", x, y)
        try:
           self.board[x][y] = "Q"
        except IndexError as err:
            logging.error("Error placing queen %i,%i: %s", x, y,err)
            return
        self.count += 1

    def check_n_place_queen(self,x,y):
        logging.debug("check_n_place_queen %i,%i", x,y)
        try:
            if self.check_queen(x,y) == 0:
                logging.debug("placing queen at %i,%i", x,y)
                self.board[x][y] = "Q"
            else:
                return -1
        except IndexError as err:
            logging.error("Error placing queen %i,%i: %s", x, y,err)
            return -1
        self.count += 1
        return 0

    def check_queen(self, x, y):
        logging.debug("check_queen %i,%i", x, y)
        #logging.debug(self.print_board())
        count = 0

        for i in range(self.n):
            if self.board[i][y] == "Q" and i != x:
                logging.debug("X FAIL!! %i,%i ",i,y)
                #self.board[i][y] = "X"
                count += 1
            if self.board[x][i] == "Q" and i != y:
                logging.debug("Y FAIL!! %i,%i",x,i)
                #self.board[x][i] = "X"
                count += 1

        # checking diagonal
        if x <= y:
            start_x = 0
            start_y = y - x
        else:
            start_x = x - y
            start_y = 0

        while start_x < self.n and start_y < self.n:
            if self.board[start_x][start_y] == "Q" and start_x != x and start_y != y:
                logging.debug("Diag FAIL 1 !! %i,%i", start_x, start_y)
                #self.board[start_x][start_y] = "X"
                count += 1
            start_x += 1
            start_y += 1

        if x <= y:
            start_x = x - ((self.n - 1) - y)    # board offset is 0 so need to decrement board size by 1
            start_y = self.n -1 # board offset is 0 so need to decrement board size by 1
        else:
            start_x = 0
            start_y = y + x

        while start_x < self.n and start_y >= 0 and start_y < self.n and x >= 0:
            if self.board[start_x][start_y] == "Q" and start_x != x:
                logging.debug("Diag FAIL 2!! %i,%i", start_x, start_y)
                #self.board[start_x][start_y] = "X"
                count += 1
            start_x += 1
            start_y -= 1
        if count == 0:
            logging.debug("Verified %i,%i", x, y)
            return 0
        else:
            logging.debug("Found %i misplaced queens", count)
            return count

    def verify_board(self):
        logging.debug("verify_board")
        x = 0
        y = 0
        queens_failed = 0

        # Checking X and Y
        for row in self.board:
            for cell in row:
                if cell == "Q":
                    logging.debug("Found One! %i,%i",x,y)
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


def solver(board,x,y):
    logging.debug("solver %i,%i", x, y)
    row = x
    col = 0

    while board.count < board.n:
        logging.debug("solver:while %i < %i", board.count, board.n)
        placed_queen = board.check_n_place_queen(row,col)

        if placed_queen == 0:
            logging.info("Placed queen# %i at position: %i,%i ", board.count,row,col)
            ret_val = solver(board,row+1,col)
            if ret_val == -1:
                logging.debug("unable to place queen on row: %i", row+1)
                logging.debug("Removing queen: %i,%i",row,col)
                board.board[row][col] = "_"
                board.count -= 1
                col += 1
                if col == board.n:
                    return -1
            else:
                col = 0
        else:
            col += 1
            if col == board.n:
                return -1


    if board.count == board.n:
        return

def main():

    size4 = Board(100)
    solver(size4,0,0)
    size4.print_board()

if __name__ == '__main__':
	main()
