class Checker:
    def __init__(self):
        None
    # Returns True if the win condition is met, otherwise returns False
    def win_checker(self, move_input):
        board = self
        board_reversed = self[::-1]
        x = len(board)
        i = int(0)
        j = int(0)
        try:
            move_input[0] = int(move_input[0])
            move_input[1] = int(move_input[1])
        except ValueError:
            return False
        if move_input[0] < 0 or move_input[1] < 0:
            return False
        if move_input[0] > len(self) or move_input[1] > len(self):
            return False
        # Row check
        for _ in range(0,x):
            if board[move_input[0]][_] == "O": # pylint: disable=unsubscriptable-object
                i += 1
            if board[move_input[0]][_] == "X": # pylint: disable=unsubscriptable-object
                j += 1
        if x in (i,j):
            return True
        i = int(0)
        j = int(0)
        # Column check
        for _ in range(0,x):
            if board[_][move_input[1]] == "O": # pylint: disable=unsubscriptable-object
                i += 1
            if board[_][move_input[1]] == "X": # pylint: disable=unsubscriptable-object
                j += 1
        if x in (i,j):
            return True
        # Diagonal check
        i = int(0)
        j = int(0)
        for _ in range(0,x):
            if board[_][_] == "O": # pylint: disable=unsubscriptable-object
                i += 1
            if board[_][_] == "X": # pylint: disable=unsubscriptable-object
                j += 1
        if x in (i,j):
            return True
        # Second diagonal check
        i = int(0)
        j = int(0)
        for _ in range(0,x):
            if board_reversed[_][_] == "O": # pylint: disable=unsubscriptable-object
                i += 1
            if board_reversed[_][_] == "X": # pylint: disable=unsubscriptable-object
                j += 1
        if x in (i,j):
            return True
        return False
