import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def find_empty_tile(self):
        """Find the next empty tile indicated with 0."""
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return r, c
        return None, None

    def checker(self, guess, row, col):
        """Check if guess can be placed at board[row][col]."""
        # check row
        if guess in self.board[row]:
            return False

        # check column
        col_list = [self.board[i][col] for i in range(9)]
        if guess in col_list:
            return False

        # check 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        matrix = [
            self.board[x][y]
            for x in range(start_row, start_row + 3)
            for y in range(start_col, start_col + 3)
        ]
        if guess in matrix:
            return False

        return True

    def solve(self):
        """Main solver function."""
        row, col = self.find_empty_tile()

        if row is None:
            return True

        for guess in range(1, 10):
            if self.checker(guess, row, col):
                self.board[row][col] = guess

                if self.solve():
                    return True

        self.board[row][col] = 0
        return False

def is_valid_start(board):
    solver = SudokuSolver(board)
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val != 0:
                board[r][c] = 0  # Temporarily clear to check
                if not solver.checker(val, r, c):
                    return False
                board[r][c] = val
    return True


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver & Checker")

        self.entries = [[None for _ in range(9)] for _ in range(9)]

        # Create 9x9 grid
        for r in range(9):
            for c in range(9):
                e = tk.Entry(root, width=2, font=("Arial", 18), justify="center")
                e.grid(row=r, column=c, padx=2, pady=2)
                self.entries[r][c] = e

        # Default board data
        self.default_board = [
            [0, 0, 7, 0, 3, 0, 8, 0, 0],
            [0, 0, 0, 2, 0, 5, 0, 0, 0],
            [4, 0, 0, 9, 0, 6, 0, 0, 1],
            [0, 4, 3, 0, 0, 0, 2, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 5, 8, 0, 0, 0, 6, 7, 0],
            [5, 0, 0, 1, 0, 8, 0, 0, 9],
            [0, 0, 0, 5, 0, 3, 0, 0, 0],
            [0, 0, 2, 0, 9, 0, 5, 0, 0]
        ]

        # Buttons Row (Row 9)
        tk.Button(root, text="Load Board", command=self.load_default_board).grid(row=9, column=0, columnspan=3, sticky="nsew")
        tk.Button(root, text="Check Board", command=self.check_user_board).grid(row=9, column=3, columnspan=3, sticky="nsew")
        tk.Button(root, text="Clear", command=self.clear_grid).grid(row=9, column=6, columnspan=3, sticky="nsew")

        # Solve Button Row (Row 10)
        tk.Button(root, text="Solve", command=self.solve_puzzle).grid(row=10, column=0, columnspan=9, sticky="nsew")

    def get_board(self):
        """Read the board from GUI entries."""
        board = []
        for r in range(9):
            row = []
            for c in range(9):
                val = self.entries[r][c].get()
                if val.isdigit():
                    row.append(int(val))
                else:
                    row.append(0)
            board.append(row)
        return board

    def set_board(self, board):
        """Display a board in GUI."""
        for r in range(9):
            for c in range(9):
                self.entries[r][c].delete(0, tk.END)
                if board[r][c] != 0:
                    self.entries[r][c].insert(0, str(board[r][c]))

    def solve_puzzle(self):
        board = self.get_board()

        if not is_valid_start(board):
            messagebox.showerror("Error", "Invalid puzzle setup!")
            return

        solver = SudokuSolver(board)
        if solver.solve():
            self.set_board(solver.board)
        else:
            messagebox.showerror("Error", "No solution found!")

    def clear_grid(self):
        for r in range(9):
            for c in range(9):
                self.entries[r][c].delete(0, tk.END)

    def load_default_board(self):
        self.set_board(self.default_board)

    def check_user_board(self):
        board = self.get_board()
        if any(0 in row for row in board):
            messagebox.showerror("Error", "Board is not complete!")
            return
        if is_valid_start(board):
            messagebox.showinfo("Result", "Congratulations! The solution is valid!")
        else:
            messagebox.showerror("Error", "The solution is incorrect.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
