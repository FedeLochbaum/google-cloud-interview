# - One can use recursion functions ( which at the end simulates the behavior of a simple stack )
# - Or one can simulate the recursion with a stack
  
def fact(n): return 1 if n == 1 else n * fact(n-1)

def stack_fact(n):
  if n == 0: return 1
  stack = []
  res = 1

  for i in range(1, n + 1): stack.append(i)

  while stack: res *= stack.pop()

  return res

def reverse(str): return '' if str == '' else reverse(str[1:]) + str[0]

def gcd(self, a, b): return a if b == 0 else self.gcd(b, a % b)


# a recursive function we simply call the function itself according to the recurrence relation until we reach the base case

# Pascal's triangle are a series of numbers arranged in the shape of triangle.
# In Pascal's triangle, the leftmost and the rightmost numbers of each row are always 1
