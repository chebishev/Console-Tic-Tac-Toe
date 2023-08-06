def check_for_win(players, board, size):
    """
    :param players: Getting the player who is in turn in order to check if wins
    :param board: Checking current the current state of all possible winning combinations:
    2 diagonals, 3 rows, 3 cols (in case of board size 3x3)
    :param size: Again it is used as final point of iteration
    :return: Game is won or deque is rotated with the next player
    """
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
