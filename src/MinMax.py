from Board import *
from Utils import *

class MinMax(object):
    def __init__(self):
        pass

    def play_move(self, core):
        pass

    def min_max(self, core, depth, maximizing_player):
        if maximizing_player: #max
            # Set the initial best value to negative infinity
            best_value = float('-inf')
            # Loop through all possible moves
            for move in available_moves(core.board.board):
                # Make the move on a copy of the current state
                new_state = make_move(core.board.board, move)
                # Recursively call min_max with the new state and depth-1
                value = self.min_max(new_state, depth-1, False)
                # Update the best value if the value is greater
                best_value = max(best_value, value)
            return best_value
        else: #min
            # Set the initial best value to positive infinity
            best_value = float('inf')
            # Loop through all possible moves
            for move in available_moves(core.board.board):
                # Make the move on a copy of the current state
                new_state = make_move(core.board.board, move)
                # Recursively call min_max with the new state and depth-1
                value = self.min_max(new_state, depth-1, True)
                # Update the best value if the value is less
                best_value = min(best_value, value)
            return best_value

    # To get the best move, loop through all possible moves and call min_max on each one
    # Return the move with the highest value if the player is maximizing, or the lowest value if the player is minimizing
    def get_best_move(self, core, depth, maximizing_player):
        best_move = None
        if maximizing_player:
            best_value = float('-inf')
            for move in available_moves(core.board.board):
                new_state = make_move(core.board.board, move)
                value = self.min_max(new_state, depth-1, False)
                if value > best_value:
                    best_value = value
                    best_move = move
        else:
            best_value = float('inf')
            for move in available_moves(core.board.board):
                new_state = make_move(core.board.board, move)
                value = self.min_max(new_state, depth-1, True)
                if value < best_value:
                    best_value = value
                    best_move = move
        return best_move