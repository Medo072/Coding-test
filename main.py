from zero import ZeroClient
import tkinter as tk
from tkinter import messagebox

class TicTacToeClient:
    def __init__(self):
        self.client = ZeroClient("0.0.0.0", 5559)
        # self.server.connect("tcp://127.0.0.1:4242")
        self.player = 1
        self.root = tk.Tk()
        self.buttons = []

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), width=6, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, sticky='nsew')
                self.buttons.append(button)


    def make_move(self, row, col):
        player = self.get_player()
        self.client.call("set_current_position", (row, col))
        self.client.call("set_current_player", msg=player)
        if self.client.call("make_move", None):
            self.update_board()
            winner = self.client.call("check_winner", None)
            if winner:
                self.show_result(winner)
            else:
                self.player = 1 if self.player == 2 else 2

    def update_board(self):
        board = self.client.call("get_board", None)
        print(board)
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            if board[row][col] == "X" or board[row][col] == "O":
                button.config(text=board[row][col])
            else:
                button.config(text="")
    def get_player(self):
        return self.player  # Replace with logic to determine the current player

    def show_result(self, winner):
        if winner is not None:
            messagebox.showinfo("Game Over", "You win!")
        else:
            messagebox.showinfo("Game Over", "You lose.")
        self.client.call("reset_board", None)
        self.update_board()

if __name__ == "__main__":
    client = TicTacToeClient()
    client.root.mainloop()
