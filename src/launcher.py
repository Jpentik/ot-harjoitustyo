from tictactoe import Tictactoe

def main():
    board_input = input("Enter board size n:")
    board_size = Tictactoe.check_board(board_input)
    print(board_size)
    board = Tictactoe.create_board(board_size)
    print(board)
if __name__ == "__main__":
    main()