import numpy as np
import os

board = np.zeros((3, 3), dtype=int)


def printboard():
    for row_index, row in enumerate(board):
        for i, col in enumerate(row):
            if col == 1:
                cell = " X "
            elif col == 2:
                cell = " O "
            else:
                if row_index == len(board) - 1:
                    cell = "   "
                else:
                    cell = "___"

            if i < len(row) - 1:
                print(cell, end="|")
            else:
                print(cell, end="")

        print()



def player_mov(player):
    print(f"Player {player} turn")
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if row in range(3) and col in range(3):
                if board[row][col] == 0:
                    board[row][col] = player
                    break
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers for row and column.")




def check_win(player):
    for i in range(3):
        if np.all(board[i] == player):
            return True
        if np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player):
        return True
    if np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def check_draw():
    return np.all(board != 0)


def switch_player(current_player):
    if current_player == 1:
        return 2
    else:        
        return 1


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


def mode_Selection(): 
    print("Select game mode:")
    print("1. Player vs Player")
    print("2. Player vs Random AI")
    print("3. Player vs Smart AI")
    print("4. Player vs Minimax AI")
    
    while True:
        choice = input("Choice: ")
        if choice in ['1','2','3','4']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 4.")

  
def print_header():
    print("|=====================|")
    print("|==== TIC TAC TOE ====|")
    print("|=======   AI  =======|")
    print("|=====================|")

print_header()
mode = mode_Selection()
os.system("cls")
current_player = 1
print_header()
while True:
    if current_player == 1:
        player_mov(1)
    else:
        if mode == '1':
            player_mov(2)
        elif mode == '2':
            Random_ai_move()
        elif mode == '3':
            smart_ai_move()
        elif mode == '4':
            best_move()

    os.system("cls")
    print_header()
    printboard()
    if check_win(current_player):
        print(f"Player {current_player} wins!")
        break
    if check_draw():
        print("It's a draw!")
        break
    current_player = switch_player(current_player)
