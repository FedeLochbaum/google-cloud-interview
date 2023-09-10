# Implement Minesweeper
# Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid.
# You are given a uniform grid of gray squares in the beginning of the game.
# Each square contains either a mine (indicated by a value of 9), or an empty square.
# Empty squares have a number indicating the count of mines in the adjacent squares.
# Empty squares can have counts from zero (no adjacent mines) up to 8 (all adjacent squares are mines).

# If you were to take a complete grid, for example, you can see which squares have mines and which squares are empty:
  
# 0  0  0  0  0
# 0  0  0  0  0
# 1  1  1  0  0
# 1  9  1  0  0
# 1  2  2  1  0
# 0  1  9  1  0
# 0  1  1  1  0

# The squares with "2" indicate that there 2 mines adjacent to that particular square.

# Gameplay starts with a user un-hiding a square at random. If the square contains a mine, the game ends.
# If it is a blank, the number of adjacent mines is revealed.

# Exposing a zero means that there are no adjacent mines, so exposing all adjacent squares is guaranteed safe.
# As a convenience to the player, the game continues to expose adjacent squares until a non-zero square is reached.

# For example, if you click on the top right corner you get this ('-' means hidden):

# template<typename T> 
# class Matrix { 
#   void resize(int rows, int cols); 
#   T& at(int row, int col); 
#   int rows(); 
#   int cols(); 
# }; 

# Write functions to construct the playing field given the size and number of mines

# Give 

# 0  0  0  0  0
# 0  0  0  0  0
# 1  1  1  0  0
# -  -  1  0  0
# -  -  2  1  0
# -  -  -  1  0
# -  -  -  1  0

# returns commpleting the guesses

# 0  0  0  0  0
# 0  0  0  0  0
# 1  1  1  0  0
# 1  9  1  0  0
# 1  2  2  1  0
# 0  1  9  1  0
# 0  1  1  1  0

input = [
  ['0', '0', '0', '0', '0'],
  ['0', '0', '0', '0', '0'],
  ['1', '1', '1', '0', '0'],
  ['-', '-', '1', '0', '0'],
  ['-', '-', '2', '1', '0'],
  ['-', '-', '-', '1', '0'],
  ['-', '-', '-', '1', '0']
]

expected = [
  ['0', '0', '0', '0', '0'],
  ['0', '0', '0', '0', '0'],
  ['1', '1', '1', '0', '0'],
  ['1', '9', '1', '0', '0'],
  ['1', '2', '2', '1', '0'],
  ['0', '1', '9', '1', '0'],
  ['0', '1', '1', '1', '0']
]

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

MINE = '9'

class MinesWeeper(object):
  def __init__(self, matrix):
    self.matrix = matrix
    self.R= len(self.matrix)
    self.C = len(self.matrix[0])
  
  def is_valid(self, r, c): return 0 <= r < self.R and 0 <= c < self.C

  def print_minesweeper(self):
    for row in self.matrix:
      print(' '.join(row))
  
  def is_the_unique_missing_to_be_a_bomb(self, point, hollow):
    val = self.matrix[point[0]][point[1]]
    if val == MINE or val == '-' or val == '0': return False
    val = int(val)
    for dr, dc in directions:
      r, c = point[0] + dr, point[1] + dc
      if self.is_valid(r, c):
        neighbor = self.matrix[r][c]
        if (neighbor == MINE or neighbor == '-'): val -= 1
    
    return val == 0

  def count_of_mines(self, point):
    row, col = point
    count = 0
    for dr, dc in directions:
      r, c = row + dr, col + dc
      if self.is_valid(r, c):
        neighbor = self.matrix[r][c]
        if neighbor == MINE: count += 1
    
    return count

  def get_deduction(self, point):
    row, col = point
    mine_count = 0
    for dr, dc in directions:
      r, c = row + dr, col + dc
      if self.is_valid(r, c):
        neighbor = self.matrix[r][c]
        if (self.is_the_unique_missing_to_be_a_bomb((r, c), point)): return MINE
        if neighbor == MINE: mine_count += 1
    return str(mine_count)
  
  def complete_mines_weeper(self):
    mines = []
    for row_i in range(len(self.matrix)):
      for col_i in range(len(self.matrix[row_i])):
        if self.matrix[row_i][col_i] == '-':
          element = self.get_deduction((row_i, col_i))
          if (element == MINE): mines.append((row_i, col_i))
          self.matrix[row_i][col_i] = element

    for mine in mines:
      for dr, dc in directions:
        r, c = mine[0] + dr, mine[1] + dc
        if self.is_valid(r, c):
          self.matrix[r][c] = str(self.count_of_mines((r, c)))

minesWeeper = MinesWeeper(input)
minesWeeper.complete_mines_weeper()

print(minesWeeper.matrix == expected)
