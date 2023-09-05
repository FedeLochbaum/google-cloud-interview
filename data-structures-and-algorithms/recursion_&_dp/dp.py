# DP motivation, it is recomputing values repeatedly

# Normally, DP without memoization is known as backtracking
# The intuition behind dynamic programming is that we trade space for time

# One can think of dynamic programming as a table-filling algorithm: you know the calculations you have to do,
# so you pick the best order to do them in and ignore the ones you don't have to fill in.

# 1. Optimization problems
# 2. Combinatorial problems

# Space complexity: O(n)
def fib(n):
  if n <= n: return n

  return fib(n-1) + fib(n-2)

# Using memo
# Space complexity: O(n)
def fib(n, memo):
  if n <= 1: return n

  if not n in memo: memo[n] = fib(n-1, memo) + fib(n-2, memo)

  return memo[n]

# Iterative
def fib_it(n):
  if n <= 1: return n
  
  fib = [0] * (n + 1)
  fib[1] = 1

  for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

  return fib[n]

# def counting_paths(grid, r, c): , using DP: O(n^2), using common recursion: O(2^n^2)

def climbStairs(n):
  if n == 1 or n == 2: return n

  dp = [0] * (n + 1)
  dp[1] = 1; dp[2] = 2

  for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

  return dp[n]
