#!/usr/bin/env python

import sys
import getopt
import logging

#logging.basicConfig(level=logging.ERROR)

class Board:

    def __init__(self,n):
        self.n = n     # Size of board and number of queens to be placed
        self.count = 0 # Number of queens placed
        self.board = [ ["_"] * n for unused in range(n)]
        self.solutions = {}
        self.solutions_count = 0

    def print_board(self):
        for row in range(0,self.n):
            for col in range(0,self.n):
                print(self.board[col][row]," ", end='')
            print()


    def board_2_string(self):
        response = ""
        for x in self.board:
            response = response.join(x)
        logging.debug(response)
        return response

    def place_queen(self,x,y):
        logging.debug("place_queen %i,%i", x, y)
        try:
           self.board[x][y] = "Q"
        except IndexError as err:
            logging.error("Error placing queen %i,%i: %s", x, y,err)
            return
        self.count += 1

    def remove_queen(self,x,y):
        logging.info("solver: Removing queen: %i,%i", x, y)
        self.board[x][y] = "_"
        #logging.debug(self.print_board())
        self.count -= 1
        return

    def check_n_place_queen(self,x,y):
        logging.debug("check_n_place_queen %i,%i", x,y)
        try:
            if self.check_queen(x,y) == 0:
                logging.debug("check_n_place_queen: placing queen at %i,%i", x,y)
                self.board[x][y] = "Q"
            else:
                return -1
        except IndexError as err:
            logging.error("check_n_place_queen: Error placing queen %i,%i: %s", x, y,err)
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
                count += 1
            if self.board[x][i] == "Q" and i != y:
                logging.debug("Y FAIL!! %i,%i",x,i)
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
            if x + y >= self.n:
                start_x = (x + y)-(self.n - 1)
                start_y = self.n -1
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

        return queens_failed

log = logging.getLogger(__name__)


def solver(board,x,y):
    log.debug("solver %i,%i", x, y)
    row = y
    col = 0

    while board.count < board.n:
        log.info("solver current state: "
                      " solutions: %i "
                      " placed_queens: %i "
                      " n: %i -- "
                      " x: %i  "
                      " y: %i ", board.solutions_count, board.count, board.n, col, row)
        placed_queen = board.check_n_place_queen(col,row)

        if placed_queen == 0:
            log.info("solver: Placed queen# %i at position: %i,%i ", board.count,col,row)
            #log.debug(board.print_board())
            ret_val = solver(board,col,row+1)
            if ret_val == -1:
                log.info("solver: unable to place queen on row: %i", row+1)
                board.remove_queen(col, row)
                col += 1
                if col >= board.n:
                    return -1
            elif ret_val == 66:
                board.remove_queen(col,row)
                col += 1
        else:
            col += 1
            if col >= board.n:
                return -1

    if board.count == board.n:
        log.info("solver:Found a solution: ")
        board.solutions_count += 1
        #log.debug("%s",board.board_2_string())
        log.debug("\n")
        #log.debug(board.print_board())
        #user_input = input("Some input please: ")
        #board.solutions.update(board.board_2_string())

        return 66

def main(argv):

    n = 0
    try:
        opts, args = getopt.getopt(argv, "hvn:")
    except getopt.GetoptError:
        print('test.py -n 8')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -n 8')
            sys.exit()
        elif opt in ("-v", "--verbose"):
            logging.basicConfig(level=logging.DEBUG)
        elif opt in ("-n"):
            n = int(arg)
    size = Board(n)
    solver(size,0,0)
    print("Solutions found ",size.solutions_count)


if __name__ == '__main__':
	main(sys.argv[1:])
