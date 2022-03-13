import numpy as np


# saving the game state in an array
board = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype=str)

# storing every possible rectangle in an array
valid_values = np.array(
    [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [9, 10], [10, 11], [11, 12], [13, 14], [14, 15],
     [15, 16], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 15], [12, 16]
     ], dtype=str)


# displaying the game in the terminal
def display_game():
    print(board)


# takes 2 squares from player 1 and updates the game if the 2 squares are valid otherwise the player will be asked to
# choose a valid rectangle
def player1_turn():
    x, y = input("Player 1 turn: ").split(", ")
    if is_valid(x, y):
        update_game(x, y)
    else:
        print("Choose a valid rectangle: ")
        player1_turn()


# takes 2 squares from player 2 and updates the game if the 2 squares are valid otherwise the player will be asked to
# choose a valid rectangle
def player2_turn():
    x, y = input("Player 2 turn: ").split(", ")
    if is_valid(x, y):
        update_game(x, y)
    else:
        print("Choose a valid rectangle: ")
        player2_turn()


# this function checks if the squares chosen by the player are valid or not
def is_valid(a, b):
    rectangle = [a, b]
    for i in range(len(valid_values)):
        if (a == valid_values[i][0] or a == valid_values[i][1]) and (b == valid_values[i][0] or b == valid_values[i][1]):
            valid_values[np.where(valid_values == a)] = 'X'
            valid_values[np.where(valid_values == b)] = 'X'
            return True
    else:
        return False


# updating the game by replacing the chosen squares with 'X' and then display the game
def update_game(a, b):
    board[np.where(board == a)] = 'X'
    board[np.where(board == b)] = 'X'
    display_game()


# the function checks if a player win the game
def is_winner():
    for i in range(len(valid_values)):
        if valid_values[i][0] != 'X' and valid_values[i][1] != 'X':
            return False
    else:
        return True


display_game()

while True:
    if is_winner():
        print("player 2 wins!")
        break
    else:
        player1_turn()

    if is_winner():
        print("player 1 wins!")
        break
    else:
        player2_turn()
