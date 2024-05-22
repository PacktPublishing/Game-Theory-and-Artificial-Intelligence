# tictactoe_board.py
from tictactoe_types import Move, Player

class TicTacToeBoard:
    """
    Represents the Tic Tac Toe board and handles the game state.
    """
    def __init__(self):
        self.board = [None] * 9

    def make_move(self, move: Move, player: Player):
        """
        Places the player's mark on the board at the specified position.
        """
        if self.board[move.position] is None:
            self.board[move.position] = player

    def undo_move(self, move: Move):
        """
        Removes the player's mark from the board at the specified position.
        """
        self.board[move.position] = None

    def available_moves(self):
        """
        Returns a list of available moves on the board.
        """
        return [Move(i) for i, x in enumerate(self.board) if x is None]

    def is_winner(self, player: Player) -> bool:
        """
        Checks if the specified player has won the game.
        """
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def is_full(self) -> bool:
        """
        Checks if the board is full.
        """
        return all(x is not None for x in self.board)
