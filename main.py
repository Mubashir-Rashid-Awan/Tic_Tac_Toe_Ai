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


current_player = 1
while True:
    if current_player == 1:
        player_mov(current_player)
    else:
        Random_ai_move()
    os.system("cls")
    printboard()
    if check_win(current_player):
        print(f"Player {current_player} wins!")
        break
    if check_draw():
        print("It's a draw!")
        break
    current_player = switch_player(current_player)
