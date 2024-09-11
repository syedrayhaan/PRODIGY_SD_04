# PRODIGY_SD_04
# Sudoku Solver

## Description

The **Sudoku Solver** project is a Python-based program that automatically solves Sudoku puzzles using the backtracking algorithm. The program takes an unsolved Sudoku grid as input and explores possible solutions to fill in the missing numbers, ensuring the correct arrangement according to the game's rules. This project demonstrates the use of recursive backtracking, a powerful algorithmic approach for solving constraint satisfaction problems like Sudoku.

## Features

- **Automated Solving**: Uses backtracking to explore all possible combinations and find the correct solution for the given Sudoku puzzle.
- **Validation Checks**: Ensures that each number placement adheres to Sudoku rules (no duplicates in rows, columns, or 3x3 sub-grids).
- **User-Friendly Output**: Displays the original unsolved Sudoku grid and the fully solved grid in a clear and readable format.
- **Efficient Algorithm**: The backtracking approach ensures that the solution is found efficiently, even for complex puzzles.

## How It Works

1. The program reads the input Sudoku grid, where empty cells are represented by `0`.
2. It attempts to fill each empty cell with numbers from 1 to 9 while checking if the placement is valid.
3. If a placement leads to a valid state, it proceeds to the next cell; if not, it backtracks and tries the next number.
4. The process continues until the entire grid is solved.

## Usage

1. Clone the repository to your local machine.
2. Run the `sudoku_solver.py` file.
3. Input your unsolved Sudoku puzzle or use the default example provided in the code.
4. The solved Sudoku grid will be displayed on the screen.

## Example

```plaintext
Original Sudoku Board:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Solved Sudoku Board:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## Future Enhancements

- Add a graphical user interface (GUI) for a more interactive user experience.
- Implement support for reading Sudoku puzzles from external files or user input.
- Optimize the algorithm further to handle larger grids or different puzzle variations.
