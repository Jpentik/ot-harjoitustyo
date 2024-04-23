import unittest
from tictactoe import Tictactoe


class TestTictactoe(unittest.TestCase):
    def setUp(self):
        self.board = Tictactoe.create_board(3)

    def test_default_board_initialization_ok(self):
        self.testboard = self.board
        self.assertEqual(self.testboard, [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])

    def test_launcher_accepts_positive_board_size(self):
        self.testboard = 4
        self.assertEqual(self.testboard, Tictactoe.check_board(4))

    def test_negative_integer_board_defaults_to_3(self):
        self.testboard = 3
        self.assertEqual(self.testboard, Tictactoe.check_board(-1))

    def test_non_integer_board_defaults_to_3(self):
        self.testboard = 3
        self.assertEqual(self.testboard, Tictactoe.check_board("A"))
