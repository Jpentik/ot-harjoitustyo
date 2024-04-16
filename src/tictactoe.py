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


	# Winning row checker
	def row_checker(board, wincount):
		row_length = len(board[0])
		print(row_length)
		i = 0
		j = 0
		k = 0
		while i < row_length - wincount +1:
			print(i)
			i += 1
		return board

board = Tictactoe.create_board(10)
board = [[1, 1, 1, 1, 1],[4, 5, 6, 6, 6],[7, 8, 9, 9, 9]]
luku = 0
#print(board[luku][luku] == board[luku][luku])
#print(board)
Tictactoe.row_checker(board,1)