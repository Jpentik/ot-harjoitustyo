# 3x3 game board initialized by default

class Tictactoe:
	# Initialization
	def __init__(self):
		self.board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		print(self.board[0])
		print(self.board[1])
		print(self.board[2])
	
	# Creates a board of size n*n
	def create_board(size):
		row = []
		x = range (size)
		for n in x:
			row.append(1)
		#print(row)
		board = []
		for n in x:
			board.append(row)
		#print(board)
		return board


Tictactoe()