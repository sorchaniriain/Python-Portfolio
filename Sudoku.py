# This program will solve a given Sudoku puzzle
# Below is the 2D template for the board. The zero's signify an empty box


def empty_squares(board):
    """
    function to detect and return the coordinates of an empty square
    :param board: partially filled 2D board
    :return: int, int
    """
    for i in range(0, 9):
        for j in range(1, 9):
            if board[i][j] == 0:
                print("Empty Square Found at position [ " + str(i) + ", " + str(j) + "] ")
               # return i, j
    return None



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
def print_board():
    """
    function to print the board
    :param board: the 2D board
    :return: None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 :
                print(" | ", end="")
            if j ==8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")



print_board()
empty_squares(board)

