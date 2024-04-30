import unittest
from tictactoe import Tictactoe
from winchecker import Checker

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

    def test_checker_rejects_negative_integer(self):
        self.testboard = self.board
        self.assertFalse(Checker.win_checker(self.testboard, [-1,-1]))

    def test_checker_rejects_non_integer_input(self):
        self.testboard = self.board
        self.assertFalse(Checker.win_checker(self.testboard, ['A', 'A']))

    def test_checker_rejects_integer_exceeding_board_size(self):
        self.testboard = self.board
        self.assertFalse(Checker.win_checker(self.testboard, [4,4]))

    def test_checker_returns_non_winning_condition(self):
        self.testboard = self.board
        self.assertFalse(Checker.win_checker(self.testboard, [0,0]))
    
    def test_checker_finds_winning_x_row(self):
        self.testboard = ["X", "X", "X"], ["-", "-", "-"], ["-", "-", "-"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))
    
    def test_checker_finds_winning_O_row(self):
        self.testboard = ["O", "O", "O"], ["-", "-", "-"], ["-", "-", "-"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))

    def test_checker_finds_winning_x_column(self):
        self.testboard = ["X", "-", "-"], ["X", "-", "-"], ["X", "-", "-"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))
    
    def test_checker_finds_winning_O_column(self):
        self.testboard = ["O", "-", "-"], ["O", "-", "-"], ["O", "-", "-"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))

    def test_checker_finds_winning_x_diagonal(self):
        self.testboard = ["X", "-", "-"], ["-", "X", "-"], ["-", "-", "X"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))

    def test_checker_finds_winning_O_diagonal(self):
        self.testboard = ["O", "-", "-"], ["-", "O", "-"], ["-", "-", "O"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))

    def test_checker_finds_winning_x_reverse_diagonal(self):
        self.testboard = ["-", "-", "X"], ["-", "X", "-"], ["X", "-", "-"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))

    def test_checker_finds_winning_O_reverse_diagonal(self):
        self.testboard = ["-", "-", "O"], ["-", "O", "-"], ["O", "-", "-"]
        self.assertTrue(Checker.win_checker(self.testboard, [0,0]))