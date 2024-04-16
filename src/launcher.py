from tictactoe import Tictactoe

def main():
    board_input = input("Enter board size n:")
    board_size = Tictactoe.check_board(board_input)
    board = Tictactoe.create_board(board_size)
    turn_count = int(0)
    max_turns = len(board)**2
    while True:
        for _ in range(board_size):
            print(board[_])
        print("---")
        if turn_count < max_turns:
            move_input = input("Enter new move: column,row ")
        else:
            print("The game is a draw")
            break
        if Tictactoe.move_advance(board, move_input) is True:
            turn_count += 1
        else:
            print("Move was not accepted")
        if Tictactoe.win_checker(board) is True:
            print("The last move won the game")
            break
if __name__ == "__main__":
    main()
