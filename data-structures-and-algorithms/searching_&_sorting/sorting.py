# - Bubblesort
#   1) Compare a pair of adjacent items (a, b),
#   2) Swap that pair if the items are out of order (in this case, when a > b),
#   3) Repeat Step 1 and 2 until we reach the end of array
#     (the last pair is the (N-2)-th and (N-1)-th items as we use 0-based indexing),
#   4) By now, the largest item will be at the last position.
#     We then reduce N by 1 and repeat Step 1 until we have N = 1

# TODO: Bubblesort

# - Selectionsort
#     1) Find the position X of the smallest item in the range of [L...N−1],
#     2) Swap X-th item with the L-th item,
#     3) Increase the lower-bound L by 1 and repeat Step 1 until L = N-2

# TODO: Selectionsort


# - Insertionsort
#   1) Start with one card in your hand,
#   2) Pick the next card and insert it into its proper sorted order,
#   3) Repeat previous step for all cards

# TODO: Insertionsort


# - Mergesort
#   1) Merge each pair of individual element (which is by default, sorted) into sorted arrays of 2 elements,
#   2) Merge each pair of sorted arrays of 2 elements into sorted arrays of 4 elements,
#     Repeat the process...,
#   3) Final step: Merge 2 sorted arrays of N/2 elements (for simplicity of this discussion, we assume that N is even) to obtain a fully sorted array of N elements

# TODO: Mergesort ( not easy to implement )
# it requires additional O(N) storage during merging operation

# - Quicksort
# To partition A[i..j], we first choose A[i] as the pivot p.

# The remaining items (i.e., A[i+1..j]) are divided into 3 regions:

#   1) S1 = A[i+1..m] where items are ≤ p,
#   2) S2 = A[m+1..k-1] where items are ≥ p, and
#   3) Unknown = A[k..j], where items are yet to be assigned to either S1 or S2.

# TODO: Quicksort
# The best case scenario of Quick Sort occurs when partition always splits the array into two equal halves, like Merge Sort.


# - Random Quicksort
# instead of implement the pivot selecton, the pivot is selected randomly



# IMPLEMENTATONS

# Bubble Sort:
# Time Complexity: O(n^2) in the WORST and average cases, O(n) in the BEST case (when the array is already sorted)
def bubble_sort(arr):
  n = len(arr)
  
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      # Swap if the element found is greater than the next element
      if arr[j  ] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
        swapped = True
    
    # If no two elements were swapped in the inner loop, the array is already sorted
    if not swapped: break

# Selection Sort:
# Time Complexity: O(n^2) in all cases (worst, average, and best).
def selection_sort(arr):
  n = len(arr)

  for i in range(n):
    # Find the minimum element in the remaining unsorted array
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j

    # Swap the found minimum element with the first element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort:
# Time Complexity: O(n^2) in the worst and average cases, O(n) in the best case (when the array is already sorted).
def insertion_sort(arr):
  n = len(arr)

  for i in range(1, n):
    curr = arr[i]

    # Move elements of arr[0..i - 1], that are greater than curr,
    # to one position ahead of their current position
    j = i - 1
    while j >= 0 and curr < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1

    # Insert the curr into the correct position
    arr[j + 1] = curr

# Merge Sort:
# Time Complexity: O(n log n) in all cases (worst, average, and best).
def merge_sort(arr):
  if len(arr) > 1:
    # Find the middle of the array
    mid = len(arr) // 2

    # Split the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # Merge the sorted halves
    i = j = k = 0  # Initialize indices for left_half, right_half, and merged array
    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]; i += 1
      else:
        arr[k] = right_half[j]; j += 1
      k += 1

    # Check if any element was left in the left_half or right_half
    while i < len(left_half):
      arr[k] = left_half[i]; i += 1; k += 1

    while j < len(right_half):
      arr[k] = right_half[j]; j += 1; k += 1

# Quick Sort:
# Time Complexity: O(n^2) in the worst case (rare), O(n log n) in the average and best cases.
# Quick Sort is often faster than Merge Sort and Heap Sort in practice.
def quick_sort(arr):
  if len(arr) <= 1: return arr
  
  pivot = arr[len(arr) // 2]  # Choose a pivot element (middle of the array)
  left = [x for x in arr if x < pivot]  # Elements less than the pivot
  middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
  right = [x for x in arr if x > pivot]  # Elements greater than the pivot
  
  # Recursively sort the left and right partitions
  return quick_sort(left) + middle + quick_sort(right)

# Heap Sort:
# Time Complexity: O(n log n) in all cases (worst, average, and best).
# Heap Sort has a smaller constant factor compared to Merge Sort.
def heapify(arr, n, i):
  largest = i  # Initialize the largest element as the root
  left = 2 * i + 1
  right = 2 * i + 2

  # If the left child exists and is greater than the root
  if left < n and arr[left] > arr[largest]: largest = left

  # If the right child exists and is greater than the largest so far
  if right < n and arr[right] > arr[largest]: largest = right

  # Change the root if needed
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # Swap
    heapify(arr, n, largest)

def heap_sort(arr):
  n = len(arr)

  # Build a max heap
  for i in range(n // 2 - 1, -1, -1): heapify(arr, n, i)

  # Extract elements from the heap one by one
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum) element with the last element
    heapify(arr, i, 0)  # Call heapify on the reduced heap

# Counting Sort:
# Time Complexity: O(n + k), where n is the number of elements in the array and k is the range of input values.
# Counting Sort is linear when the range of input values is not significantly greater than the number of elements.
def counting_sort(arr):
  # Find the maximum and minimum elements in the array
  max_value = max(arr)
  min_value = min(arr)
  
  # Create a counting array to store the count of each element
  count_array = [0] * (max_value - min_value + 1)
  
  # Count the occurrences of each element in the input array
  for num in arr:
    count_array[num - min_value] += 1
  
  # Reconstruct the sorted array
  sorted_array = []
  for i, count in enumerate(count_array):
    sorted_array.extend([i + min_value] * count)
  
  return sorted_array

# Radix Sort:
# Time Complexity: O(n * k), where n is the number of elements in the array, and k is the number of digits in the maximum number.
# Radix Sort is linear for fixed-length integers.
def radix_sort(arr):
  # Find the maximum element in the array to determine the number of digits
  max_value = max(arr)
  exp = 1

  while max_value // exp > 0:
    counting_sort(arr, exp)
    exp *= 10  # Move to the next digit

# Bucket Sort:
# Time Complexity: O(n^2) in the worst case, but it can be O(n) if the input is uniformly distributed across buckets.
# It's often used with other sorting algorithms as a preprocessing step.
def bucket_sort(arr):
  if len(arr) == 0: return arr

  min_value = min(arr)
  max_value = max(arr)

  # Create buckets and distribute elements into them
  bucket_range = max_value - min_value
  bucket_size = bucket_range // len(arr) + 1
  num_buckets = (bucket_range // bucket_size) + 1
  buckets = [[] for _ in range(num_buckets)]

  for num in arr:
    index = (num - min_value) // bucket_size
    buckets[index].append(num)

  # Sort each bucket using insertion sort
  sorted_buckets = []
  for bucket in buckets:
    insertion_sort(bucket)
    sorted_buckets.extend(bucket)

  return sorted_buckets