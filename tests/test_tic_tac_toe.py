import unittest
from src.base import Base
from src.game_board import GameFunctions
from unittest.mock import patch


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = GameFunctions()
        Base.board = [[Base.empty for _ in range(Base.columns)] for _ in range(Base.rows)]

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


    @patch('builtins.input', side_effect=['9', '!', '5'])
    def test_invalid_move(self, mock_input):
        result = self.game.next_move()
        print("Print invalid move of 9 and !")
        self.assertEqual(result,'5') # Exits loop after valid move




