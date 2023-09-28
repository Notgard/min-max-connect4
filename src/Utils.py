def is_column_full(board, col):
        return board[0][col] != 0

def available_moves(board):
    moves = []
    for col in range(7):
        if not is_column_full(board, col):
            moves.append(col)
    return moves

def make_move(board, move, player):
    new_board = board.copy()  # Make a copy of the current board
    for row in range(5, -1, -1):
        if new_board[row][move] == 0:
            new_board[row][move] = player
            break
    return new_board