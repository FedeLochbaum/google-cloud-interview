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



