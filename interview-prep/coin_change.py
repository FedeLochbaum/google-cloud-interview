# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

def coin_change(coins, amount):
  memo = [float('inf')] * (amount + 1)
  memo[0] = 0 # base case

  for coin in coins:
    for i in range(coin, amount + 1):
      # memo[i] is the minimumm between the curent memo for the differreces AND the memo for take one coin more of value coin 
      memo[i] = min(memo[i], memo[i - coin] + 1)

  return memo[amount] if memo[amount] != float('inf') else -1

print(coin_change([1, 2, 5], 11)) # 3
print(coin_change([2], 3)) # -1
print(coin_change([1], 0)) # 0