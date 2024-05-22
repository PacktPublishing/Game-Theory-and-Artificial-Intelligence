# tictactoe_ai.py
from tictactoe_board import TicTacToeBoard
from tictactoe_types import Move, Player

class TicTacToeAI:
    """
    Minimax algorithm implementation for Tic Tac Toe.
    """
    def __init__(self, player: Player):
        self.player = player
        self.evaluated_states = 0

    def best_move(self, board: TicTacToeBoard) -> Move:
        """
        Determines the best move for the current player using the Minimax algorithm.
        """
        best_value = -float('inf')
        best_move = None
        for move in board.available_moves():
            board.make_move(move, self.player)
            value = self._evaluate(board, False)
            board.undo_move(move)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

    def _evaluate(self, board: TicTacToeBoard, is_maximizing: bool) -> float:
        """
        Recursively evaluates the board states to determine the best move.
        """
        self.evaluated_states += 1  # Increment the counter
        if board.is_winner(self.player):
            return 1
        elif board.is_winner(self.player.opponent()):
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_value = -float('inf')
            for move in board.available_moves():
                board.make_move(move, self.player)
                value = self._evaluate(board, False)
                board.undo_move(move)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = float('inf')
            for move in board.available_moves():
                board.make_move(move, self.player.opponent())
                value = self._evaluate(board, True)
                board.undo_move(move)
                best_value = min(best_value, value)
            return best_value
