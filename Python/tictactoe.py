import tkinter as tk

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    return False

def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

def on_click(row, col):
    global player, player_x_score, player_o_score
    if board[row][col] == '-':
        board[row][col] = player
        buttons[row][col].config(text=player)
        
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            if player == 'X':
                player_x_score += 1
            else:
                player_o_score += 1
            update_scoreboard()
            reset_board()
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            reset_board()
        else:
            player = 'O' if player == 'X' else 'X'

def reset_board():
    global board
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'
            buttons[i][j].config(text='')

def update_scoreboard():
    score_label.config(text=f"Player X: {player_x_score}\nPlayer O: {player_o_score}")

player = 'X'
board = [['-' for _ in range(3)] for _ in range(3)]
player_x_score = 0
player_o_score = 0

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 30), width=4, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, sticky="nsew")

reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_board)
reset_button.grid(row=3, column=1, columnspan=3, sticky="nsew")

score_label = tk.Label(root, text=f"Player X: {player_x_score}\nPlayer O: {player_o_score}", font=('Arial', 14))
score_label.grid(row=4, column=1, columnspan=3)

root.mainloop()
