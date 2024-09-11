def print_board(board):
    """Function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def find_empty(board):
    """Function to find an empty spot on the board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # row, col
    return None


def is_valid(board, num, pos):
    """Function to check if the current number is valid at the given position."""
    # Check the row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the 3x3 sub-grid
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    """Function to solve the Sudoku board using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Example Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku Board:")
print_board(board)

if solve(board):
    print("\nSolved Sudoku Board:")
    print_board(board)
else:
    print("No solution exists.")
