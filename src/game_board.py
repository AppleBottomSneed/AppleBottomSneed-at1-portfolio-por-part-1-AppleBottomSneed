from src.base import Base

class GameFunctions:
    def __init__(self):
        Base.board = [Base.empty] * 9


    def print_board(self):
        print(Base.board[0], "|", Base.board[1], "|", Base.board[2])
        print("---------")
        print(Base.board[3], "|", Base.board[4], "|", Base.board[5])
        print("---------")
        print(Base.board[6], "|", Base.board[7], "|", Base.board[8])
        print()

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for wc in win_conditions:
            if Base.board[wc[0]] == Base.board[wc[1]] == Base.board[wc[2]] != Base.empty:
                print("Player", Base.board[wc[0]], "wins!")
                exit(0)

        # Check for tie
        if Base.empty not in Base.board:
            print("It's a tie!")
            exit(0)

    # Get next move
    def next_move(self):
        while True:
            player = Base.p1 if Base.board.count(Base.empty) % 2 == 1 else Base.p2
            move = input("Next move for player " + player + " (0-8): ")
            if move.isdigit() and 0 <= int(move) <= 8 and Base.board[int(move)] == Base.empty:
                Base.board[int(move)] = player
                break
            else:
                print("Invalid move, try again.")


