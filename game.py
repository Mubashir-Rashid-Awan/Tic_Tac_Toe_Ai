import numpy as np
from board import board

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