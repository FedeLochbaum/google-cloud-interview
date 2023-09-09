# A “word square” is an ordered sequence of K different words of length K that,
# when written one word per line, reads the same horizontally and vertically. For example:

# BALL
# AREA
# LEAD
# LADY

# In this exercise you're going to create a way to find word squares.

# First, design a way to return true if a given sequence of words is a word square.

# Second, given an arbitrary list of words, return all the possible word squares it contains. Reordering is allowed.

# For example, the input list

# [AREA, BALL, DEAR, LADY, LEAD, YARD]

# should output

# [(BALL, AREA, LEAD, LADY), (LADY, AREA, DEAR, YARD)]

# Finishing the first task should help you accomplish the second task.

def is_word_square(words):
  K = len(words)
  for i in range(K): # ( 0 to K-1 )
    if len(words[i]) != K: return False
    for j in range(i + 1, K):
      if words[j][i] != words[i][j]: return False
  
  return True

def is_valid_prefix(prefix, words):
  for word in words:
    if not word.startswith(prefix): return False
  return True

def word_squares_from(current_square, prefixes):
  if len(current_square) == len(current_square[0]): # I ended and it is a valid word square
    return [tuple(current_square)]

  squares = []
  col = len(current_square)
  prefix = ''.join(row[col] for row in current_square)

  if not prefix in prefixes: return []

  for word in prefixes[prefix]:
    if is_valid_prefix(word, prefixes[prefix]):
      current_square.append(word)
      squares += word_squares_from(current_square, prefixes)
      current_square.pop()
  return squares

def word_squares(list):
  prefixes = {}
  # Generate all possible prefixes
  for word in list:
    for i in range(len(word)):
      prefix = word[:i]
      if prefix not in prefixes: prefixes[prefix] = []

      prefixes[prefix].append(word)
  
  result = []
  for word in list:
    result += word_squares_from([word], prefixes)

  return result
    
print(is_word_square(('BALL', 'AREA', 'LEAD', 'LADY')) == True)

print(word_squares(
  ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']) == [('BALL', 'AREA', 'LEAD', 'LADY'), ('LADY', 'AREA', 'DEAR', 'YARD')]
)