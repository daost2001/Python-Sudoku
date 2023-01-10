import random

# This function generates a random Sudoku board using a backtracking algorithm
def generate_board():
  board = [[0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]]
  for i in range(10):
      row = random.randrange(9)
      col = random.randrange(9)
      val = random.randrange(9)
      if (is_valid(board, row, col, val)):
          board[row][col] = val
  # Use backtracking to fill in the board
  if solve_board(board, 0, 0):
    return board
  return None

# This function solves the Sudoku board using backtracking
def solve_board(board, i, j):
  # Check if we have reached the end of the board
  if i == 9:
    return True

  # Move to the next cell if the current cell is already filled
  if board[i][j] != 0:
    return solve_board(board, i + (j+1)//9, (j+1)%9)

  # Try placing all values from 1 to 9
  for value in range(1,10):
    if is_valid(board, i, j, value):
      board[i][j] = value
      # Recurse to fill in the rest of the board
      if solve_board(board, i + (j+1)//9, (j+1)%9):
        return True
      # Backtrack if the board is invalid
      board[i][j] = 0
  return False

# This function checks if it is valid to place a value at the given position on the board
def is_valid(board, row, col, value):
  # Check row and column constraints
  for i in range(9):
    if board[row][i] == value or board[i][col] == value:
      return False

  # Check 3x3 block constraints
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[start_row + i][start_col + j] == value:
        return False
  return True

def is_valid_sudoku(board):
    # check rows
    for row in board:
        if not all(row.count(num) == 1 for num in range(1,10)):
            return False

    # check columns
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        if not all(column.count(num) == 1 for num in range(1,10)):
            return False

    # check 3x3 squares
    for i in range(3):
        for j in range(3):
            square = []
            for row in range(i*3, i*3+3):
                for col in range(j*3, j*3+3):
                    square.append(board[row][col])
            if not all(square.count(num) == 1 for num in range(1,10)):
                return False

    # if we get here, the board is valid
    return True


def show_board(board):
    for row in board:
        print(row)

for i in range(100):
    board = generate_board()
    show_board(board)
    print(is_valid_sudoku(board))
