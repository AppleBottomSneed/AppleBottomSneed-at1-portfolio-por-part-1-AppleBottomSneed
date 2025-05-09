class Base:
    p1 = "X"
    p2 = "O"
    empty = " "
    rows, columns = (3, 3)

    def __init__(self):
        self.board = [[self.empty for _ in range(self.columns)] for _ in range(self.rows)]

