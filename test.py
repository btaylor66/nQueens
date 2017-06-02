#!/usr/bin/env python

import unittest
import nqueens

class TestBoardMethods(unittest.TestCase):

    def test_initialize(self):
        test = nqueens.Board(4)
        self.assertEqual(test.n, 4, 'Incorrect Board Size')

    def test_horizontal_fail(self):
        test = nqueens.Board(4)
        test.place_queen(0,0)
        test.place_queen(0,2)
        self.assertEqual(test.verify_board(),1, 'Looking for 1 Queen misplaced')

    def test_vertical_fail(self):
        test = nqueens.Board(4)
        test.place_queen(0,1)
        test.place_queen(3,1)
        self.assertEqual(test.verify_board(),1, 'Looking for 1 Queen misplaced')

    def test_diagonal_fail(self):
        test = nqueens.Board(4)
        test.place_queen(0,0)
        test.place_queen(3,3)
        self.assertEqual(test.verify_board(),1, 'Looking for 1 Queen misplaced')

    def test_x_out_of_scope(self):
        test = nqueens.Board(4)
        test.place_queen(0,0)
        test.place_queen(5,3)
        self.assertEqual(test.verify_board(),'Error placing queen in  0 , 5  :  list assignment index out of range','Expecting Error placing Queen')

    def test_correct_size4(self):
        test = nqueens.Board(4)
        test.place_queen(0,2)
        test.place_queen(1,0)
        test.place_queen(2,3)
        test.place_queen(3,1)
        self.assertEqual(test.verify_board(),0, 'Board should pass')

    def test_horizontal_fail_size1000(self):
        test = nqueens.Board(1000)
        test.place_queen(0,0)
        test.place_queen(0,962)
        self.assertEqual(test.verify_board(),1, 'Looking for 1 Queen misplaced')

    def test_vertical_fail_size1000(self):
        test = nqueens.Board(1000)
        test.place_queen(0,1)
        test.place_queen(850,1)
        self.assertEqual(test.verify_board(),1, 'Looking for 1 Queen misplaced')

    def test_diagonal_fail_size1000(self):
        test = nqueens.Board(1000)
        test.place_queen(0,0)
        test.place_queen(999,999)
        self.assertEqual(test.verify_board(),1, 'Looking for 1 Queen misplaced')

if __name__ == '__main__':
    unittest.main()