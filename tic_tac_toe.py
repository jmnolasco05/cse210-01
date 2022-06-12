"""
Tic-Tac-Toe
Author: Joan Nolasco 
"""


def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"

    print("Welcome to the game")

    display_board(board)

    while not (has_winner(board, current_player) or is_draw(board)):
        selection = input(
            f"{current_player}'s turn to choose a square (1-9): ")

        if is_valid(selection, board):
            position = int(selection) - 1
            board[position] = current_player

            current_player = get_next_player(current_player)

            display_board(board)

        else:
            print("Invalid selection.")

    print("Good game. Thanks for playing!")


def display_board(board):
    print('\n')
    print(f'{board[0]} | {board[1]} | { board[2]}')
    print('- + - + -')
    print(f'{board[3]} | {board[4]} | { board[5]}')
    print('- + - + -')
    print(f'{board[6]} | {board[7]} | { board[8]}')
    print("\n")


def has_winner(board, current_player):
    horizontal_win = (board[0] == board[1] == board[2]) or (
        board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8])

    vertical_win = (board[0] == board[3] == board[6]) or (
        board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8])

    diagonal_win = (board[0] == board[4] == board[8]) or (
        board[2] == board[4] == board[6])

    if horizontal_win or vertical_win or diagonal_win:
        print(f"{get_next_player(current_player)} has won.\n")
        return True

    return False


def is_draw(board):
    uniqueElements = set(board)

    if(len(uniqueElements) == 2):
        print("It is a draw.\n")
        return True

    return False


def get_next_player(current_player):

    if current_player in (None, 'O'):
        next_player = 'X'
    else:
        next_player = 'O'

    return next_player


def is_valid(selection, board):
    return selection.isdigit() and selection in board


if __name__ == '__main__':
    main()
