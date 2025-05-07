import unittest
from src.base import Base
from src.game_board import GameFunctions


class TestTicTacToe(unittest.TestCase):

    def test_check_winner_x_wins(self):
        #Down
        Base.board = ["X", "O", "X",
                      "X", "O", "O",
                      "X", "X", "O"]
        with self.assertRaises(SystemExit):
            GameFunctions.check_winner(self)

    def test_check_winner_o_wins(self):
        #Diagonal
        Base.board = ["O", "X", "O",
                      "X", "O", "O",
                      "O", "X", "X"]
        with self.assertRaises(SystemExit):
            GameFunctions.check_winner(self)

    def test_check_winner_tie(self):
        #None
        Base.board = ["O", "X", "O",
                      "X", "X", "O",
                      "O", "O", "X"]
        with self.assertRaises(SystemExit):
            GameFunctions.check_winner(self)


