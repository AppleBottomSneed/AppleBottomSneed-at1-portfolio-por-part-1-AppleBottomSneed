from src.base import Base

class GameFunctions:
    def __init__(self):
        Base.board = [[Base.empty for _ in range (Base.columns)] for _ in  range(Base.rows)]


    def print_board(self):
        for i in range(Base.rows):
            row = " | ".join(Base.board[i])
            print(row)
            if i < Base.rows - 1:
                print("-" * (Base.rows * 3))

    def check_winner(self):
        flattened_list = [box for row in Base.board for box in row] #flattens Base.board
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for wc in win_conditions:
            if flattened_list[wc[0]] == flattened_list[wc[1]] == flattened_list[wc[2]] != Base.empty:
                print("Player", flattened_list[wc[0]], "wins!")
                exit(0)

        # Check for tie
        if Base.empty not in flattened_list:
            print("It's a tie!")
            exit(0)

    # Get next move
    def next_move(self):
        while True:
            flattened_list = [box for row in Base.board for box in row]
            player = Base.p1 if flattened_list.count(Base.empty) % 2 == 1 else Base.p2
            move = input("Next move for player " + player + " (0-8): ")
            if move.isdigit() and 0 <= int(move) <= 8 and flattened_list[int(move)] == Base.empty:
                flattened_list[int(move)] = player
                break
            else:
                print("Invalid move, try again.")


