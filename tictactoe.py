import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.configure(bg='#4B8BBE')  # Python blue

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Arial", 40), width=5, height=2,
                               command=lambda x=i: self.make_move(x),
                               bg='#FFD43B', activebackground='#FFE873')  # Python yellow
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(button)

        reset_button = tk.Button(self.window, text="Reset", font=("Arial", 20),
                                 command=self.reset_game, bg='#FFD43B', activebackground='#FFE873')
        reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def make_move(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
