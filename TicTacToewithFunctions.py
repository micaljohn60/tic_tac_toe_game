def create_board():
    return [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


def row_winner(board, player):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2]:
            print("------------- Row Winner is ------ " + player)
            winner = True
            return winner


def col_winner(board, player):
    for row in range(len(board)):
        for col in range(len(list(zip(board)))):
            if board[0][col] == board[1][col] == board[2][col]:
                print("------------- Col Winner is ------ " + player)
                winner = True
                return winner


def diag_winner(board, player):
    if (
        board[0][0] == board[1][1] == board[2][2]
        or board[2][0] == board[1][1] == board[0][2]
    ):
        print("------------- Diag Winner is ------ " + player)
        winner = True
        return winner


def evaluate(board, player):
    winner = False

    if (
        row_winner(board, player)
        or col_winner(board, player)
        or diag_winner(board, player)
    ):
        winner = True

    return winner


def place_player(board, player):
    print("This is player ---- " + player + " ----")
    inpt = input("Enter your point ")
    for row in range(len(board)):
        for col in range(len(list(zip(board)))):
            if board[row][col] == inpt:
                board[row][col] = player
                return board


def playGame():
    board = create_board()
    winner = False
    turn = 0
    players = ["X", "O"]
    count = 10

    for row in range(len(board)):
        print("----------------")
        print(board[row])
    print("----------------")

    while winner == False and count > 1:
        player = players[turn]
        turn = (turn + 1) % 2
        board = place_player(board, player)
        winner = evaluate(board, player)
        count -= 1
        if count == 1:
            print("Tie")
        if winner != False:
            break

        for row in range(len(board)):
            print("----------------")
            print(board[row])
        print("----------------")

    return player


playGame()
