
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  n = 1
  for i in nums:
    if i == n: n+=1
    if n == 4: return True

  return False

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))