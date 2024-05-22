# tictactoe_types.py
from enum import Enum

class Player(Enum):
    """
    Represents a player in the Tic Tac Toe game.
    """
    X = 'X'
    O = 'O'

    def opponent(self):
        """
        Returns the opponent of the current player.
        """
        return Player.X if self == Player.O else Player.O

class Move:
    """
    Represents a move in the Tic Tac Toe game.
    """
    def __init__(self, position: int):
        self.position = position
