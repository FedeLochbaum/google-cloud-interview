# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Rules:
# 1) Any live cell with fewer than two live neighbors dies as if caused by under-population.
# 2) Any live cell with two or three live neighbors lives on to the next generation.
# 3) Any live cell with more than three live neighbors dies, as if by over-population.
# 4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
# Given the current state of the m x n grid board, return the next state.

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

class GameOfLife():
  def __init__(self, initial_board):
    self.board = initial_board

  def is_alive(self, point): return self.board[point[0]][point[1]] == 1

  def print_board(self):
    for row in self.board: print(row)

  def simulate_game(self, times):
    for _ in range(times):
      self.simulate_life()

  def is_valid_point(self, r, c): return 0 <= r < len(self.board) and 0 <= c < len(self.board[0])
  
  def neighbors_alive(self, point):
    neighbors_alive = 0
    for dr, dc in directions:
      r, c = point[0] + dr, point[1] + dc
      if self.is_valid_point(r, c):
        neighbors_alive += 1 if self.is_alive((r, c)) else 0
    return neighbors_alive

  def simulate_life(self):
    moves = [] # done to avoid copy the board

    for row in range(len(self.board)):
      for col in range(len(self.board[row])):
        count_alive = self.neighbors_alive((row, col))
        if self.is_alive((row, col)):
          if count_alive < 2 or count_alive > 3: moves.append((row, col, 0)) # 1 and 3
        else: # rule 4
          if count_alive == 3: moves.append((row, col, 1)) # 4

    for row, col, n in moves: self.board[row][col] = n

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
game = GameOfLife(board)
game.simulate_game(1)
game.print_board()

  # [0,0,0]
  # [1,0,1]
  # [0,1,1]
  # [0,1,0]