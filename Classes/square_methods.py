from . import square
from Resources import constants


def make_empty_grid():
    squares = []
    for j in range(0, constants.SCREEN_Y, constants.RECTANGLE_Y):
        for i in range(0, constants.SCREEN_X, constants.RECTANGLE_X):
            temp = square.square(i,j)
            squares.append(temp)
    return squares


def range_finder(value):
    if value in range(0, 200):
        return 0
    elif value in range(200, 400):
        return 1
    else:
        return 2


def find_block(squares, x, y):
    i_value, j_value = range_finder(x), range_finder(y)
    return squares[constants.INDICES[(i_value, j_value)]]


def game_outcome(squares):
    """
    print ( "current value of squares is " , )
    for i in squares:
        print(i.symbol_value,end=' ')
    print()
    """
    # ROW CHECKS
    if squares[0].symbol_value == squares[1].symbol_value == squares[2].symbol_value and squares[0].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[0].symbol_value
    if squares[3].symbol_value == squares[4].symbol_value == squares[5].symbol_value and squares[3].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[3].symbol_value
    if squares[6].symbol_value == squares[7].symbol_value == squares[8].symbol_value and squares[6].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[6].symbol_value
    # COLUMN CHECKS
    if squares[0].symbol_value == squares[3].symbol_value == squares[6].symbol_value and squares[0].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[0].symbol_value
    if squares[1].symbol_value == squares[4].symbol_value == squares[4].symbol_value and squares[1].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[1].symbol_value
    if squares[2].symbol_value == squares[5].symbol_value == squares[8].symbol_value and squares[2].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[2].symbol_value
    # DIAGONAL CHECKS
    if squares[0].symbol_value == squares[4].symbol_value == squares[8].symbol_value and squares[0].symbol_value is not None:
        print("completed because of indices 0,1,2")
        return squares[0].symbol_value
    if squares[2].symbol_value == squares[4].symbol_value == squares[6].symbol_value and squares[2].symbol_value is not None:
        print("completed because of indices 2,4,6 ")
        return squares[2].symbol_value
    return None


def find_available(grid):
    options = []
    print("In find available")
    print(grid)
    for i in range(len(grid)):
        if grid[i] == -1:
            options.append(i)
    return options
