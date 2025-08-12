#Sudoku Solver & Checker

A simple Python-based Sudoku application with a graphical interface built using Tkinter.  
This app allows you to input a Sudoku puzzle, check its validity, solve it automatically, or try solving a built-in default puzzle yourself.

## Features

- **Manual Input:** Enter your own Sudoku puzzle in the grid and have it solved.
- **Load Default Puzzle:** Quickly load a pre-defined Sudoku board and try to solve.
- **Check Board:** Verify if your filled board follows Sudoku rules.
- **Clear Board:** Clear the grid of values.
- **Solve Puzzle:** Automatically solve the puzzle using a backtracking algorithm.

## Requirements

- Python 3.8 or later
- Tkinter (usually included with Python installations)
> install Tkinter if not already available
> Ubuntu/Debian:
```bash
	sudo apt-get update
	sudo apt-get install python3-tk
```
## How to Run

1. Open a terminal or command prompt.
2. Navigate to the folder containing the program
3. Run: python3 SudokuApp.py

## How To Use

### Manual Entry
- Click on any grid cell and type a number from 1 to 9.
- Leave cells blank for empty tiles (they are treated as 0 internally).

### Load Board

- Click Load Board to insert the default Sudoku puzzle into the grid.

### Check Board
- Once you fill in all cells, click Check Board to verify if your solution is correct.

### Clear Board
- Click Clear to empty the grid and start fresh.

### Solve Puzzle
- Click Solve to let the algorithm fill in the solution for the current puzzle.
