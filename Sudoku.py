# This program will solve a given Sudoku puzzle

# Below is the 2D template for the board. The zero's signify an empty box
board = [
    [5, 0, 0, 0, 1, 0, 0, 0, 4],
    [2, 7, 4, 0, 0, 0, 6, 0, 0],
    [0, 8, 0, 9, 0, 4, 0, 0, 0],
    [8, 1, 0, 9, 0, 4, 0, 0, 0],
    [0, 0, 2, 0, 3, 0, 1, 0, 0],
    [7, 0, 6, 0, 9, 1, 0, 5, 8],
    [0, 0, 0, 5, 0, 3, 0, 1, 0],
    [0, 0, 5, 0, 0, 0, 9, 2, 7],
    [1, 0, 0, 0, 2, 0, 0, 0, 3]
]
# Function to print the current board
for i in range(len(board)):
    print(board[i], sep="\n")




