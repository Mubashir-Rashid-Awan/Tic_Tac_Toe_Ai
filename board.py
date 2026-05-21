import numpy as np

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