# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1

# Example a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

# There are two subarrays meeting the criterion:[1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has  elements.

# Function Description

# Complete the pickingNumbers function in the editor below.

# pickingNumbers has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the length of the longest subarray that meets the criterion
# Input Format

# The first line contains a single integer , the size of the array .
# The second line contains  space-separated integers, each an .

# Constraints

# The answer will be .
# Sample Input 0

# 6
# 4 6 5 3 3 1
# Sample Output 0

# 3
# Explanation 0

# We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e.,  and ), so we print the number of chosen integers, , as our answer.

# Sample Input 1

# 6
# 1 2 2 3 1 2
# Sample Output 1

# 5
# Explanation 1

# We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e., , , and ), so we print the number of chosen integers, , as our answer.

def picking_numbers(items):
  items.sort()
  _max = 0
  for i in range(len(items)):
    count = 1

    for j in range(i + 1, len(items)):
      if abs(items[j] - items[i]) <= 1: count += 1
      else: break

    _max = max(_max, count)

  return _max

print(picking_numbers([1, 1, 2, 2, 4, 4, 5, 5, 5])) # [4, 4, 5, 5, 5]
print(picking_numbers([4, 6, 5, 3, 3, 1])) # [4, 3, 3] 
print(picking_numbers([1, 2, 2, 3, 1, 2])) # [1, 2, 2, 1, 2]