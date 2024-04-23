class Tictactoe:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    def check_board(self):
        try:
            board_input = int(self)
        except ValueError:
            print("Input is not an integer. Using default size 3.")
            board_input = 3
        if board_input < 1:
            print("Input integer is zero or negative. Using default size 3.")
            board_input = 3
        return board_input
    # Creates a board of size n*n
    def create_board(self):
        board = [["-" for _ in range(self)] for _ in range(self)]
        return board
    # Returns True if a move is legal, otherwise returns False
    def move_advance(self, move_input):
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
