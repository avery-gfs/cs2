// The board is a list of rows, each row is a list of numbers (cells)
// where each cell is either 0 (inactive) or 1 (active)

// Starting board
const initial = [
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

const height = initial.length   // Number of rows
const width = initial[0].length // Number of columns

// Generate an empty board
function blankBoard() {
  // Somehow even worse than Python
  return Array(height).fill(null).map(() => Array(width).fill(0));
}

// ---------- Begin Simulation Logic ----------

// Print board as a 2D grid of characters where active cells
// are shown as 'X' and inactives as ' '
function display(board) {
  // Loop through each row in board
  for (const row of board) {
    let rowStr = "";

    // Loop through each cell value in current row
    for (const cell of row) {
      // Check if cell is active
      // (avoid ternary to keep things simple)
      if (cell === 1) {
        rowStr += "X";
      } else {
        rowStr += " ";
      }
    }

    // Print current row string with pipes as side borders
    console.log("|" + rowStr + "|");
  }
}

// Get the cell value at the given row and column position
// or 0 if the position is past the edge of the board
function getCell(board, row, col) {
  if (row < 0 || row >= height || col < 0 || col >= width) {
    return 0; // Position is outside of the board dimensions
  }

  return board[row][col];
}

// Count the number of actice cells bordering the cell at the given position
function countNeighbors(board, row, col) {
  let total = 0;

  // Loop through every combination of dr and dc
  // dr and dc are row and column offsets, each either -1, 0, or 1
  for (const dr of [-1, 0, 1]) {
    for (const dc of [-1, 0, 1]) {
      // Add neighbor cell value to total
      total += getCell(board, row + dr, col + dc);
    }
  }

  // The code above counts the value of the cell at the current position
  // itself, which we don't want, so we subtract it out
  return total - board[row][col];
}

// From the current board, generate the new board for the next simulation step
function update(board) {
  // Don't want to update the current board while we're reading from it
  // so make a new board to put the changes into
  const newBoard = blankBoard();

  // Loop over every board position
  for (let row = 0; row < height; row++) {
    for (let col = 0; col < width; col++) {
      const neighbors = countNeighbors(board, row, col)

      // A cell will be active in the new board if it has 3 neighbors in the
      // current board, or if it has two neighbors in the current board and
      // is active, and will be inactive otherwise
      if (neighbors == 3 || board[row][col] && neighbors == 2) {
        newBoard[row][col] = 1;
      } else {
        newBoard[row][col] = 0;
      }
    }
  }

  return newBoard;
}

// ---------- End Simulation Logic ----------

let board = initial;

for (let step = 0; step < 60; step++) {
  process.stdout.write("\x1Bc");              // Clear the screen
  display(board);                             // Display the board
  console.log(`\nstep: ${step}`);             // Display step number
  await new Promise(r => setTimeout(r, 100)); // Pause 100ms
  board = update(board);                      // Update board state
}
