# This question is designed to help you get a better understanding of basic heap operations.

# There are  types of query:

# " " - Add an element  to the heap.
# " " - Delete the element  from the heap.
# "" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

# Input Format

# The first line contains the number of queries, .
# Each of the next  lines contains one of the  types of query.

# Constraints


# Output Format

# For each query of type , print the minimum value on a single line.

# Sample Input

# STDIN       Function
# -----       --------
# 5           Q = 5
# 1 4         insert 4
# 1 9         insert 9
# 3           print minimum
# 2 4         delete 4
# 3           print minimum
# Sample Output

# 4  
# 9 
# Explanation

# After the first  queries, the heap contains {}. Printing the minimum gives  as the output. Then, the  query deletes  from the heap, and the  query gives  as the output.

import heapq

def add_elem(heap, arg): heapq.heappush(heap, arg)
def del_elem(heap, arg): heap.remove(arg); heapq.heapify(heap)

apply_command = { 1: add_elem, 2: del_elem }
count_of_queries = int(input())
heap = []
for _ in range(count_of_queries):
  query = input()
  if query == '3': print(heap[0]); continue
  command, arg = list(map(int, query.split(' ')))
  apply_command[command](heap, arg)