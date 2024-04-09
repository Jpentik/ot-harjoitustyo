import unittest
from tictactoe import Tictactoe

class TestTictactoe(unittest.TestCase):
    def setUp(self):
        self.board = Tictactoe.create_board(3)
        
    def test_default_board_initialization_ok(self):
        self.tictactoe = self.board
        self.assertEqual(self.tictactoe, [[1, 1, 1],[1, 1, 1],[1, 1, 1]])