# Given an integer array nums, return the length of the longest strictly increasing ( subsequence )

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

def length_of_lis_iterative(nums): # much more efficient
  n = len(nums)
  dp = [1] * n

  for i in range(n):
    for j in range(i):
      if nums[i] > nums[j]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)

def length_of_lis_with_dp(nums, prev_index, current_index, memo):
  if current_index == len(nums): return 0

  if memo[prev_index][current_index] != -1: return memo[prev_index][current_index]

  taken = 0
  if prev_index == -1 or nums[current_index] > nums[prev_index]:
    taken = 1 + length_of_lis_with_dp(nums, current_index, current_index + 1, memo) # call recursively assumming that the current elem was taken

  not_taken = length_of_lis_with_dp(nums, prev_index, current_index + 1, memo) # not taking the current element

  memo[prev_index][current_index] = max(taken, not_taken) # max of both
  return memo[prev_index][current_index]


def length_of_lis(nums): n = len(nums); return length_of_lis_with_dp(nums, -1, 0, [[-1] * n for _ in range(n)])

print(length_of_lis([10,9,2,5,3,7,101,18])) # 4
print(length_of_lis([0,1,0,3,2,3])) # 4
print(length_of_lis([7,7,7,7,7,7,7])) # 1