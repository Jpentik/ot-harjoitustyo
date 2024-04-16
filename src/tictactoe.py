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
    # Main gameplay loop
    def play_tictactoe(self):
        print("Hello world")
