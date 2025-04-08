import time
import os

# The board is a list of rows, each row is a list of numbers (cells)
# where each cell is either 0 (inactive) or 1 (active)

# Starting board
initial = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]

height = len(initial)   # Number of rows
width = len(initial[0]) # Number of columns

# Generate an empty board with height and width matching the
# initial board and filled with zeros
def blankBoard():
    # We can't use [[0] * width] * height
    # cause of silly Python aliasing
    return [[0] * width for _ in range(height)]

# ---------- Begin Simulation Logic ----------

# Print board as a 2D grid of characters where active cells
# are shown as 'X' and inactives as ' '
def display(board):
    pass # Change

# Get the cell value at the given row and column position
# or 0 if the position is past the edge of the board
def getCell(board, row, col):
    pass # Change

# Count the number of actice cells bordering the cell at the given position
def countNeighbors(board, row, col):
    pass # Change

# From the current board, generate the new board for the next simulation step
def update(board):
    return board # Change
    
# ---------- End Simulation Logic ----------

board = initial

for step in range(60):
    os.system("clear")     # Clear the screen
    display(board)         # Display the board
    print(f"step: {step}") # Display step number
    time.sleep(0.1)        # Pause 100ms
    board = update(board)  # Update board state
