class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                move = input("Enter your move as row,col (e.g., 1,2): ")
                row, col = map(int, move.strip().split(","))
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
            except Exception:
                pass
            print("Invalid input. Please enter row,col (0-2).")
