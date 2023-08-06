def print_board(players, board, size, begin=False):
    """
    :param players: getting the deque with the players in order to print the first player
    :param board:  getting the board to print its state at every move
    :param size:  getting the size of the board as final point of iteration
    :param begin: if True the game starts with board filled with numbers as positions
    in any other case it prints the current status of the board
    :return: None
    """
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
