def binary_search(array, elem): # The array must to be sorted
  left = 0
  right = len(array) - 1

  while(left <= right):
    mid = left + int(right - left / 2)
    if mid == elem: return True

    if (elem < mid): right = mid - 1; continue

    left = mid + 1
  
  return False
