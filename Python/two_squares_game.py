import numpy as np

# board, display board
board = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype=str)

valid_values = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [9, 10], [10, 11], [11, 12], [13, 14], [14, 15],
     [15, 16], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [
         7, 11], [8, 12], [9, 13], [10, 14], [11, 15], [12, 16]
     ], dtype=str)


def display_game():
    print(board)

# player turns
def player1_turn():
    x, y = input("Player 1 turn: ").split(", ")
    if is_valid(x, y):
        update_board(x, y)
    else:
        print("Choose a valid rectangle!")
        player1_turn()


def player2_turn():
    x, y = input("Player 2 turn: ").split(", ")
    if is_valid(x, y):
        update_board(x, y)
    else:
        print("Choose a valid rectangle!")
        player2_turn()


# valid squares
def is_valid(a, b):
    for i in range(len(valid_values)):
        if (a == valid_values[i][0] or a == valid_values[i][1]) and (b == valid_values[i][0] or b == valid_values[i][1]):
            valid_values[np.where(valid_values == a)] = 'X'
            valid_values[np.where(valid_values == b)] = 'X'       
            return True   
    return False

# update board
def update_board(a, b):
    board[np.where(board == a)] = 'X'
    board[np.where(board == b)] = 'X'
    display_game()

# game-winning condition
def no_rectangles_left():
    for i in range(len(valid_values)):
        if valid_values[i][0] != 'X' and valid_values[i][1] != 'X':
            return False
    return True

display_game()

while True:
    player1_turn()
    if no_rectangles_left():
        print("Player 1 wins!")
        break
    player2_turn()
    if no_rectangles_left():
        print("Player 2 wins!")
        break
