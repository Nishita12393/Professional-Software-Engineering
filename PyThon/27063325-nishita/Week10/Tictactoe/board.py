class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\n  0   1   2")
        for idx, row in enumerate(self.grid):
            print(f"{idx} {' | '.join(row)}")
            if idx < 2:
                print("  ---------")
        print()

    def make_move(self, row, col, symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        win_states = [
            # rows
            [(0, i) for i in range(3)],
            [(1, i) for i in range(3)],
            [(2, i) for i in range(3)],
            # columns
            [(i, 0) for i in range(3)],
            [(i, 1) for i in range(3)],
            [(i, 2) for i in range(3)],
            # diagonals
            [(i, i) for i in range(3)],
            [(i, 2 - i) for i in range(3)],
        ]

        for condition in win_states:
            if all(self.grid[r][c] == symbol for r, c in condition):
                return True
        return False

    def is_game_over(self):
        return all(cell != " " for row in self.grid for cell in row)
