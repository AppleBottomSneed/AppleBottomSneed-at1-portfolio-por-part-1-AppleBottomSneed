import unittest
from src.base import Base
from src.game_board import GameFunctions


class TestTicTacToe(unittest.TestCase):

    def test_check_winner_x_wins(self):
        #Down
        Base.board = [
            ["X", "0", "X"],
            ["X", "0", "0"],
            ["X", "0", "0"],
        ]
        with self.assertRaises(SystemExit):
            print("Checking winner is X:")
            GameFunctions.check_winner(self)

    def test_check_winner_o_wins(self):
        #Diagonal
        Base.board = [
            ["0", "0", "X"],
            ["X", "0", "0"],
            ["X", "X", "0"],
        ]
        with self.assertRaises(SystemExit):
            print("Checking winner is 0:")
            GameFunctions.check_winner(self)

    def test_check_winner_tie(self):
        #None
        Base.board = ["0", "X", "0",
                      "X", "X", "0",
                      "0", "0", "X"]
        with self.assertRaises(SystemExit):
            print("Checking tie:")
            GameFunctions.check_winner(self)



