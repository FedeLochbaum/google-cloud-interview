# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def valid_parentheses(_str):
  stack = []
  delimiters = { ')': '(', '}': '{', ']': '[' } # key = close delimiterss, value: open delimiter
  for char in _str:
    if char in delimiters.values(): stack.append(char); continue # if the char is open delimiter

    if char in delimiters.keys(): # if the char is close delimiter
      if not stack: return False
      if stack.pop() != delimiters[char]: return False # if you want to close a { then, previously in the stack's top should be a }
  
  return not stack # should be empty