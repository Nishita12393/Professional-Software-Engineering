from board import Board
from player import Player

class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_turn = 0

    def start(self):
        print("Welcome to Tic-Tac-Toe!")
        self.board.display()

        while not self.board.is_game_over():
            player = self.players[self.current_turn]
            print(f"{player.name}'s Turn ({player.symbol}):")
            row, col = player.get_move(self.board)

            if self.board.make_move(row, col, player.symbol):
                self.board.display()
                if self.board.check_winner(player.symbol):
                    print(f"{player.name} wins!")
                    return
                self.current_turn = 1 - self.current_turn
            else:
                print("Invalid move. Try again.")

        print("It's a draw!")
