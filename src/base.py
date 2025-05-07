class Base:
    p1 = "X"
    p2 = "O"
    empty = " "
    rows, columns = (3, 3)
    board = [[empty for _ in range(columns)] for _ in range(rows)]
