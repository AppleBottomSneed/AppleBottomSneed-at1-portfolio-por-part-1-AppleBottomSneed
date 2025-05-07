from src.game_board import GameFunctions

def main():
    game = GameFunctions()

    while True:
        game.print_board()
        game.check_winner()
        game.next_move()

if __name__ == "__main__":
    main()