from zero import ZeroServer
from itertools import cycle
app = ZeroServer(port=5559)
class TicTacToeServer():
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 0
        self.current_position = (0, 0)

@app.register_rpc
def get_board() -> list:
    return server.board

@app.register_rpc
def check_winner() -> int:
    winner = None

    for row in server.board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            break

    for col in range(len(server.board)):
        if server.board[0][col] == server.board[1][col] == server.board[2][col] and server.board[0][col] != 0:
            winner = server.board[0][col]
            break

    if server.board[0][0] == server.board[1][1] == server.board[2][2] and server.board[0][0] != 0:
        winner = server.board[0][0]
    elif server.board[0][2] == server.board[1][1] == server.board[2][0] and server.board[0][2] != 0:
        winner = server.board[0][2]

    if all([all(row) for row in server.board]) and winner is None:
        winner = "tie"

    return winner

# @app.register_rpc
# def is_valid_move() -> int:
#     row, col = server.current_position[0], server.current_position[1]
#     return 3 > row >= 0 == server.board[row][col] and 0 <= col < 3

@app.register_rpc
def reset_board() -> int:
    server.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    server.current_player = 0
    return 1

@app.register_rpc
def set_current_position(position: tuple) -> int:
    server.current_position = position
    return 1

@app.register_rpc
def set_current_player(player: int) -> int:
    server.current_player = player
    return 1
@app.register_rpc
def make_move() -> str:
    player = server.current_player
    row, col = server.current_position[0], server.current_position[1]
    if player:
        server.board[row][col] = "X" if player == 1 else "O"
        return server.board[row][col]
    return "0"


if __name__ == "__main__":
    server = TicTacToeServer()
    app.run()
