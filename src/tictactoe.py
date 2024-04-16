class Tictactoe:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turns = 9
    def check_board(self):
        try:
            board_input = int(self)
        except ValueError:
            print("Input is not an integer. Using default size 3.")
            board_input = 3
        if board_input < 1:
            print("Input integer is negative. Using default size 3.")
            board_input = 3
        return board_input
	# Creates a board of size n*n
    def create_board(self):
        board = []
        row = []
        x = range (self)
        for _ in x:
            row.append(0)
        for _ in x:
            board.append(row)
        return board
    # Returns True if a move is legal, otherwise returns False (TBD)
    def move_advance(self, move_input):
        print(move_input)
        return True
    # Returns True if the win codition is met, otherwise returns False (TBD)
    def win_checker(self):
        return False
