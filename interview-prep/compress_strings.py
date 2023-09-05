# The Challenge
# In this exercise, you're going to decompress a compressed string.

# Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

# The input

# 3[abc]4[ab]c

# Would be output as

# abcabcabcababababc

# Other rules
# Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

# One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

# Characters allowed as input include digits, small English letters and brackets [ ].

# Digits are only to represent amount of repetitions.

# Letters are just letters.

# Brackets are only part of syntax of writing repeated substring.

# Input is always valid, so no need to check its validity.

def decompress(compressed):
  stack = []
  current_number = 0
  res = ''

  for char in compressed:
    if char.isdigit():
      current_number = current_number * 10 + int(char)
    elif char == '[':
      stack.append((current_number, res))
      current_number = 0
      res = ''
    elif char == ']':
      times, last_string = stack.pop()
      res = last_string + (res * times)
    else: res += char

  return res


print(decompress('3[abc]4[ab]c'))