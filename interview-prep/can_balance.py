# Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side
# is equal to the sum of the numbers on the other side.

# can_balance([1, 1, 1, 2, 1]) → true
# can_balance([2, 1, 1, 2, 1]) → false
# can_balance([10, 10]) → true

def can_balance(list): #Using two pointers to avoid use N space complexity
  if len(list) == 1: return False

  left, i = list[0], 1
  right, j = list[-1], len(list) - 2
  for _ in range(len(list) - 2):
    if left > right: right += list[j]; j -= 1
    else: left += list[i]; i += 1
  
  return left == right

print(can_balance([1, 1, 1, 2, 1]))
print(can_balance([2, 1, 1, 2, 1]))
print(can_balance([10, 10]))