# Given a linked list of size N, your task is to complete the function isLengthEvenOrOdd()
# which contains head of the linked list and check whether the length of linked list is even or odd.

# Input:
# The input line contains T, denoting the number of testcases. Each testcase contains two lines.
# the first line contains N(size of the linked list). the second line contains N elements of the linked list separated by space.

# Output:
# For each testcase in new line, print "even"(without quotes) if the length is even else "odd"(without quotes) if the length is odd.

# User Task:
# Since this is a functional problem you don't have to worry about input, you just have to  complete the function isLengthEvenOrOdd()
# which takes head of the linked list as input parameter and returns 0 if the length of the linked list is even otherwise returns 1.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 103
# 1 <= A[i] <= 103

# Example:
# Input:
# 2
# 3
# 9 4 3
# 6
# 12 52 10 47 95 0

# Output:
# Odd
# Even

# Explanation:
# Testcase 1: The length of linked list is 3 which is odd.
# Testcase 2: The length of linked list is 6 which is even.

# is_length_even_or_odd([9, 4, 3]) returns 1
# is_length_even_or_odd([12, 52, 10, 47, 95, 0]) returns 0


def is_length_even_or_odd(head):
  even = True
  current = head
  while (current != None):
    even = not even
    current = current.next
  return 0 if even else 1