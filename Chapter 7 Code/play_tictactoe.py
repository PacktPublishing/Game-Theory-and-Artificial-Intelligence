# play_tictactoe.py
from tictactoe_board import TicTacToeBoard
from tictactoe_types import Player, Move
from tictactoe_ai import TicTacToeAI

def main():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = TicTacToeBoard()
    player = Player.X
    ai = TicTacToeAI(player)

    while not board.is_full() and not board.is_winner(Player.X) and not board.is_winner(Player.O):
        print_board(board)
        if player == Player.X:
            move = ai.best_move(board)
        else:
            move = get_human_move(board)
        board.make_move(move, player)
        player = player.opponent()

    print_board(board)
    if board.is_winner(Player.X):
        print("Player X wins!")
    elif board.is_winner(Player.O):
        print("Player O wins!")
    else:
        print("It's a tie!")

def get_human_move(board):
    """
    Prompts the human player to enter a move and validates the input.
    """
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in [m.position for m in board.available_moves()]:
                return Move(move)
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

def print_board(board):
    """
    Prints the current state of the board.
    """
    for i in range(0, 9, 3):
        row = [board.board[i + j].value if board.board[i + j] is not None else '-' for j in range(3)]
        print(' '.join(row))
    print()

if __name__ == "__main__":
    main()
