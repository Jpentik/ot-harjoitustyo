class Tictactoe:
    """Class that checks board input, creates an empty board and checks the validity of moves."""
    def __init__(self):
        """Class's constructor that creates an empty 3x3 board.

        Args:
            board: List of lists. An empty 3x3 board.
        """
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    def check_board(self):
        """Checks that input is a valid integer

        Returns:
            board_input: Board size given by user, if valid. Otherwise defaults to 3.
        """
        try:
            board_input = int(self)
        except ValueError:
            print("Input is not an integer. Using default size 3.")
            board_input = 3
        if board_input < 1:
            print("Input integer is zero or negative. Using default size 3.")
            board_input = 3
        return board_input

    def create_board(self):
        """Creates a board of size n*n.

        Returns:
            board: List of lists. Every value is symbol "-".
        """
        board = [["-" for _ in range(self)] for _ in range(self)]
        return board

    def move_advance(self, move_input):
        """Checks if the move input by user is valid.

        Args:
            move_input: List of input coordinates (row, column).

        Returns:
            True, if the move is valid, otherwise False.
        """
        board = self
        try:
            move_input[0] = int(move_input[0])
            move_input[1] = int(move_input[1])
        except ValueError:
            print("Input is not an integer")
            return False
        if move_input[0] < 0 or move_input[1] < 0:
            print("Input integer is negative")
            return False
        if move_input[0] > len(self) or move_input[1] > len(self):
            print("Input integer is outside board size")
            return False
        print(move_input)
        if board[move_input[0]][move_input[1]] == "-": # pylint: disable=unsubscriptable-object
            return True
        return False
