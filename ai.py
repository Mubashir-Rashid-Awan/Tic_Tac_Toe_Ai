import numpy as np
from board import board
from game import check_win, check_draw

def Random_ai_move():
    empty_cells = np.argwhere(board == 0)
    if len(empty_cells) > 0:
        row, col = empty_cells[np.random.choice(len(empty_cells))]
        board[row][col] = 2

def smart_ai_move():
    empty_cells = np.argwhere(board == 0)   
    for row,col in empty_cells:         # check if AI can win in the next move
        board[row][col] = 2
        if check_win(2):
            return
        board[row][col] = 0

    for row,col in empty_cells:         # check if player can win in the next move and block it
        board[row][col] = 1
        if check_win(1):
            board[row][col] = 2
            return
        board[row][col] = 0    

    if board[1][1] == 0:                 # take center if available take it
        board[1][1] = 2
        return
    
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for row, col in corners:             # take any available corner
        if board[row][col] == 0:
            board[row][col] = 2
            return
    
    Random_ai_move()                      # if no winning move, blocking move, center or corner is available, take a random move

def minimax(is_maximizing):
     
    if check_win(2):
        return 1
    if check_win(1):
        return -1
    if check_draw():
        return 0

      
    if is_maximizing:
        best_score = -1000
        empty_cells = np.argwhere(board == 0) 
        for row,col in empty_cells:
            board[row][col] = 2
            score = minimax(False)
            board[row][col] = 0
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        empty_cells = np.argwhere(board == 0) 
        for row,col in empty_cells:
            board[row][col] = 1
            score = minimax(True)
            board[row][col] = 0
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -1000
    move_row = None
    move_col = None
    empty_cells = np.argwhere(board == 0) 
    for row,col in empty_cells:
        board[row][col] = 2
        score = minimax(False)
        board[row][col] = 0
        if score > best_score:
            best_score = score
            move_row = row
            move_col = col
    if move_row is not None and move_col is not None:
        board[move_row][move_col] = 2
