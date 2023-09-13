# Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence
# of one or more dictionary words.

# Problem Constraints
# 1 <= len(A) <= 6500
# 1 <= len(B) <= 10000
# 1 <= len(B[i]) <= 20

# Input Format
# The first argument is a string, A.
# The second argument is an array of strings, B.

# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

# Example Input
# Input 1:
# A = "myinterviewtrainer",
# B = ["trainer", "my", "interview"]
# Output: 1

# Input 2:
# A = "a"
# B = ["aaa"]
# Output: 0

# Example Explanation
# Explanation 1:
# Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".
# Explanation 2:

# Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".

def word_break_with_dict(_str, _map, memo):
  if _str == '': return True

  if not _str in memo:
    memo[_str] = False
    for i in range(1, len(_str) + 1):
      left = _str[:i]
      right = _str[i:]
      if left in _map and (word_break_with_dict(right, _map, memo)):
        memo[_str] = True
        return True
  
  return memo[_str]

def word_break_with_dict2(_str, _map, _dict, memo):
  n = len(_str)

  memo = [False] * (n + 1) # possible to segment a substring
  memo[0] = True # base case, empty string
  
  max_word_len = max(len(word) for word in _dict)

  for i in range(1, n + 1):
    for j in range(min(i, max_word_len) + 1): # Check if the substring from j to i-1 is in the dictionary and if memo[j] is True.
        if memo[j] and _str[j:i] in _map:
          memo[i] = True
          break

  return memo[n]

def word_break(_str, _dict):
  dict_as_map = {}
  for word in _dict: dict_as_map[word] = True

  return 1 if word_break_with_dict2(_str, dict_as_map, _dict, {}) else 0

print(word_break('myinterviewtrainer', ["trainer", "my", "interview"])) # 1
print(word_break('a', ["aaa"])) # 0