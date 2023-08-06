from collections import deque


def check_for_draw():
    if all([all(pos.strip() for pos in row) for row in board]):
        print("Draw!")
        raise SystemExit


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - i - 1] == player_symbol for i in range(size)])
    row_win = any([all(pos == player_symbol for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(f"{player_name} won!")

        raise SystemExit

    else:
        players.rotate(1)


def place_symbol(position):
    row, col = (position - 1) // size, (position - 1) % size

    if board[row][col] != " ":
        raise ValueError

    board[row][col] = players[0][1]

    print_board()

    check_for_win()
    check_for_draw()

    choose_position()


def choose_position():
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


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

        # erase all the numbers from the board so the game can start
        for row in range(size):
            for col in range(size):
                board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
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
    print_board(True)
    choose_position()


# rotatable deque of players with their symbols in format [[player name, symbol], [player name, symbol]]
players = deque()
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
size = len(board)

start()
