# Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Problem Constraints
# 1 <= |A| <= 106
# 1 <= Ai <= 109

# Input Format
# The first argument is an integer array A.

# Output Format
# Return the majority element.

# Example Input
# A = [2, 1, 2]

# Example Output
# 2

def majority_element(A):
  bound = abs(len(A) / 2)
  _map = {}
  for a in A:
    if not a in _map: _map[a] = 0
    _map[a] += 1

  _max = A[0]
  for k in _map.keys():
    if _map[k] < bound: continue
    if _map[k] > _map[_max]: _max = k

  return _max

print(majority_element([2, 1, 2])) # 2
print(majority_element([100])) # 2