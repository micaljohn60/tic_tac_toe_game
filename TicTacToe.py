def ticTacToe():
    players = ["X", "O"]  # Define Players
    turn = 0  # players turn
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    for rows in range(len(board)):
        print(board[rows])

    count = 10
    winner = False

    if winner == False:
        while count > 0:
            player = players[turn]
            turn = (turn + 1) % len(players)
            print("This is player " + player)
            inp = input("Enter your point")

            for row in range(len(board)):
                for col in range(len(list(zip(board)))):

                    if inp == board[row][col]:

                        board[row][col] = player
                        count -= 1
                        if board[row][0] == board[row][1] == board[row][2]:
                            print("------------- Row Winner is ------ " + player)
                            winner = True
                            count = 0
                        if board[0][col] == board[1][col] == board[2][col]:
                            print("------------- Col Winner is ------ " + player)
                            winner = True
                            count = 0
                        if (
                            board[0][0] == board[1][1] == board[2][2]
                            or board[2][0] == board[1][1] == board[0][2]
                        ):
                            print("------------- Diag Winner is ------ " + player)
                            winner = True
                            count = 0

            for rows in range(len(board)):
                print(board[rows])


ticTacToe()

# class Player:
#     def __init__(self, symbol, score):
#         self.symbol = symbol
#         self.score = score
#
#
# class PlayingField:
#     def set_player(self, row, col, player):
#         self.field[row][col] = player
#
#     def check_winner(self, player):
#         board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
#         inp = input("Enter your point")
#         for row in range(len(board)):
#             for col in range(len(list(zip(board)))):
#                 if inp == board[row][col]:
#                     board[row][col] = player
#                     if board[row][0] == board[row][1] == board[row][2]:
#                         print("------------Row Winner--------------")
#                     if board[0][col] == board[0][col] == board[0][col]:
#                         print("------------Col Winner--------------")
#                     if (
#                         board[0][0] == board[1][1] == board[2][2]
#                         or board[2][0] == board[1][1] == board[0][2]
#                     ):
#                         print("------------Diag Winner-------------")
#
#
# def main():
#     players = ["X", "O"]
#     turn = 0
#     player = players[turn]
#     turn = (turn + 1) % 2
#
#     field = PlayingField()
#
#     field.check_winner(player)
#
#
# if __name__ == "__main__":
#     main()


# def row_winner(player):
#     for row in range(len(board)):
#         for col in range(len(list(zip(board)))):
#             if inp == board[row][col]:
#                 board[row][col] = player
#                 turn = (turn + 1 ) % 2
#                 count -= 1
#                 if board[row][0] == board[row][1] == board[row][2]:
#                     print("------------Row Winner--------------")
#                 else:
#                     pass
#
# def col_winnder(player):
#     for row in range(len(board)):
#         for col in range(len(list(zip(board)))):
#             if inp == board[row][col]:
#                 board[row][col] = player
#                 count -= 1
#                 if board[0][col] == board[1][col] == board[2][col]:
#                     print("------------Col Winner--------------")
# def diag_winner(player):
#     for row in range(len(board)):
#         for col in range(len(list(zip(board)))):
#             if inp == board[row][col]:
#                 board[row][col] = player
#                 count -= 1
#                 if (
#                     board[0][0] == board[1][1] == board[2][2]
#                     or board[2][0] == board[1][1] == board[0][2]
#                 ):
#                     print("------------Diag Winner-------------")

# for row in range(len(board)):
#     print(board[row])
#
# count = 10
# turn = 0
#
# for i in range(9):
#     players = ["X", "O"]
#     player = players[turn]
#     turn = (turn + 1) % 2
#     print("This is player " + player)
#
#     inp = input("Enter your point")
#     for row in range(len(board)):
#         for col in range(len(list(zip(board)))):
#             if inp == board[row][col]:
#                 board[row][col] = player
#                 count -= 1
#                 if board[row][0] == board[row][1] == board[row][2]:
#                     print("------------Row Winner--------------")
#                 if board[0][col] == board[1][col] == board[2][col]:
#                     print("------------Col Winner--------------")
#                 if (
#                     board[0][0] == board[1][1] == board[2][2]
#                     or board[2][0] == board[1][1] == board[0][2]
#                 ):
#                     print("------------Diag Winner-------------")
#     for rows in range(len(board)):
#         print(board[rows])
