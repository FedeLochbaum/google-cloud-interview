# Given a string A, partition A such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of A.

# Problem Constraints
# 1 <= length(A) <= 501

# Input Format
# The first and the only argument contains the string A.

# Output Format
# Return an integer, representing the minimum cuts needed.

# Example Input
# Input 1:

#  A = "aba"
# Input 2:

#  A = "aab"

# Example Output
# Output 1:

#  0
# Output 2:

#  1

def is_palindrome(s, start, end):
  while start < end:
    if s[start] != s[end]: return False
    start += 1
    end -= 1
  return True

def min_cut(A):
  n = len(A)
  
  min_cuts = [0] * n
  
  for end in range(1, n):
    min_cuts[end] = end
    
    for start in range(end, -1, -1):
      if is_palindrome(A, start, end):
        min_cuts[end] = 0 if start == 0 else min(min_cuts[end], min_cuts[start - 1] + 1)
  
  return min_cuts[n - 1]