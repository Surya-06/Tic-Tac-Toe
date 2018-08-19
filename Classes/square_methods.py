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
    # DEBUG STATEMENT
    print(constants.INDICES[(i_value, j_value)])
    return squares[constants.INDICES[(i_value, j_value)]]


"""
def game_state(grid):
    # ROW CHECKS -- ( MANUAL -- HAD TIME )
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]
    elif grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]
    elif grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]
    # COLUMN CHECKS
    elif grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]
    elif grid[0][1] == grid[1][1] == grid[2][1]:
        return grid[0][1]
    elif grid[0][2] == grid[1][2] == grid[2][2]:
        return grid[0][2]
    # DIAGONAL CHECKS
    elif grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]
    return False
"""


def game_outcome(squares):
    # ROW CHECKS
    if squares[0].symbol_value == squares[1].symbol_value == squares[2].symbol_value and squares[0] is not None:
        return squares[0].symbol_value
    if squares[3].symbol_value == squares[4].symbol_value == squares[5].symbol_value and squares[3] is not None:
        return squares[3].symbol_value
    if squares[6].symbol_value == squares[7].symbol_value == squares[8].symbol_value and squares[6] is not None:
        return squares[6].symbol_value
    # COLUMN CHECKS
    if squares[0].symbol_value == squares[3].symbol_value == squares[6].symbol_value and squares[0] is not None:
        return squares[0].symbol_value
    if squares[1].symbol_value == squares[4].symbol_value == squares[4].symbol_value and squares[1] is not None:
        return squares[1].symbol_value
    if squares[2].symbol_value == squares[5].symbol_value == squares[8].symbol_value and squares[2] is not None:
        return squares[2].symbol_value
    # DIAGONAL CHECKS
    if squares[0].symbol_value == squares[1].symbol_value == squares[8].symbol_value and squares[0] is not None:
        return squares[0].symbol_value
    if squares[2].symbol_value == squares[4].symbol_value == squares[6].symbol_value and squares[2] is not None:
        return squares[2].symbol_value
    return None


def find_available(grid):
    options = []
    for i in range(len(grid)):
        if grid[i] == -1:
            options.append(i)
    return options
