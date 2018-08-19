# DEBUG METHODS HERE :-p


def printer(grid_values):
    print("staring to print the grid ")
    for i in range(len(grid_values) - 1, -1, -1):
        for j in range(len(grid_values[i])):
            print(grid_values[i][j], end=' ')
        print()
    print("completed printing the grid ")


reverse_indices = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 1), 5: (1, 2), 6: (2, 0), 7: (2, 1), 8: (2, 2)}


def print_index(input):
    return reverse_indices[input]
