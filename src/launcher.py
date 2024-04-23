from tictactoe import Tictactoe
from checker import Checker

def main():
    board_input = input("Enter board size n:")
    board_size = Tictactoe.check_board(board_input)
    board = Tictactoe.create_board(board_size)
    turn_count = int(1)
    max_turns = len(board)**2
    move_input = [0,0]
    while True:
        for _ in range(board_size):
            print(board[_])
        print("----------")
        if Checker.win_checker(board, move_input) is True:
            print("The last move won the game")
            break
        if turn_count <= max_turns:
            move_input[0] = input("Enter new move: row 0-(n-1) ")
            move_input[1] = input("Enter new move: column 0-(n-1) ")
            if move_input[0] == "q" or move_input[1] == "q":
                break
        else:
            print("The game is a draw")
            break
        if Tictactoe.move_advance(board, move_input) is True:
            if turn_count % 2 == 1:
                board[move_input[0]][move_input[1]] = "X"
            if turn_count % 2 == 0:
                board[move_input[0]][move_input[1]] = "O"
            turn_count += 1
        else:
            print("Move was not accepted")
if __name__ == "__main__":
    main()
