def check_for_draw(board):
    """
    :param board: getting the board in order to check if it is filled with "X's" or "O's"
    :return: Draw if board is filled with "X's" or "O's" and the game stops
    """
    if all([all(pos.strip() for pos in row) for row in board]):
        print("Draw!")
        raise SystemExit
