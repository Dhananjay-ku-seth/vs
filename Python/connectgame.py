import numpy as np
import tkinter as tk
from tkinter import messagebox

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    return np.zeros((ROW_COUNT,COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            color = "white" if board[r][c] == 0 else ("red" if board[r][c] == 1 else "yellow")
            canvas.create_rectangle(c * SQUARESIZE, (r+1) * SQUARESIZE, (c+1) * SQUARESIZE, (r+2) * SQUARESIZE, fill="blue")
            canvas.create_oval(c * SQUARESIZE, (r+1) * SQUARESIZE, (c+1) * SQUARESIZE, (r+2) * SQUARESIZE, fill=color, outline="black")

def drop(event):
    global turn, game_over
    col = event.x // SQUARESIZE

    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, turn + 1)
        draw_board(board)

        if winning_move(board, turn + 1):
            messagebox.showinfo("Connect Four", f"Player {turn + 1} wins!")
            update_score(turn + 1)
            game_over = True

        turn += 1
        turn %= 2  # Switch turns between 0 and 1

        if not any(0 in row for row in board):
            messagebox.showinfo("Connect Four", "It's a draw!")
            game_over = True

def reset_game():
    global board, game_over
    board = create_board()
    draw_board(board)
    game_over = False

def update_score(player):
    if player == 1:
        scores[0] += 1
    elif player == 2:
        scores[1] += 1

    score_label.config(text=f"Player 1: {scores[0]}   Player 2: {scores[1]}")

# Initialize the game
root = tk.Tk()
root.title("Connect Four")

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

board = create_board()
draw_board(board)

turn = 0
game_over = False
scores = [0, 0]

canvas.bind("<Button-1>", drop)

# Scoreboard
score_label = tk.Label(root, text=f"Player 1: {scores[0]}   Player 2: {scores[1]}", font=("Arial", 16))
score_label.pack()

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 16))
reset_button.pack()

root.mainloop()
