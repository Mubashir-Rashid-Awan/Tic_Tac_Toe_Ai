import os
from board import printboard
from game import player_mov, check_win, check_draw, switch_player
from ai import Random_ai_move, smart_ai_move, best_move


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
