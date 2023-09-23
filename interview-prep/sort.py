# Return an array that contains the sorted values from the input array with duplicates removed.

# sort([]) → []
# sort([1]) → [1]
# sort([1, 1]) → [1]

def sort(arr): return sorted(set(arr))

print(sort([]))
print(sort([1]))
print(sort([1, 1]))