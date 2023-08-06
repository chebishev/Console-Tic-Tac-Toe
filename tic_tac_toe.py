from collections import deque
from pyfiglet import Figlet

from board import print_board
from draw import check_for_draw
from win import check_for_win


def place_symbol(position):
    """
    :param position: Position is number from 1 to size * size of the board
    and this function translates it to row, column from board[0][0] to board[size - 1][size - 1]
    :return: board with new player symbol on it, checks for draw or win and asks
    for the next player to choose position
    """
    row, col = (position - 1) // size, (position - 1) % size

    if board[row][col] != " ":
        raise ValueError

    board[row][col] = players[0][1]

    print_board(players, board, size)

    check_for_win(players, board, size)
    check_for_draw(board)

    choose_position()


def choose_position():
    """
    :return: returns the chosen position from 1 to size * size
    if it is not valid it raises ValueError and asks the player to choose again
    """
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position [1-{size * size}]: "))

            if 1 <= position <= size * size:
                place_symbol(position)
                break
            else:
                raise ValueError

        except ValueError:
            print(f'{players[0][0]} enter a valid position!')
            continue


def start():
    figlet = Figlet(font='slant')
    print(figlet.renderText('TIC TAC TOE'))
    player_one_name = input("Player one enter your name: ")
    player_two_name = input("Player two enter your name: ")
    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O': ").upper()

        if player_one_symbol not in ('X', 'O'):
            print("Please enter either 'X' or 'O'")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    # first printing of the board is with filled positions
    print_board(players, board, size, True)
    choose_position()


# rotatable deque of players with their symbols in format [[player name, symbol], [player name, symbol]]
players = deque()
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
size = len(board)

start()
