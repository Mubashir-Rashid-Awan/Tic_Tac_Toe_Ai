import numpy as np  
board = np.zeros((3, 3), dtype=int)
print (board)

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

