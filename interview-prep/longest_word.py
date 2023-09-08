# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
# Learning objectives
# This question gives you the chance to practice with algorithms and data structures. It’s also a good example of why careful analysis for Big-O performance is often worthwhile, as is careful exploration of common and worst-case input conditions.

# O( N * M ), with N = length of S, M = total number of characters in words
def longest_word(_str, words):
  consuming_words = {}
  res = ''
  for word in words:
    if not word[0] in consuming_words: consuming_words[word[0]] = []
    consuming_words[word[0]].append((word, word))

  for char in _str:
    if char in consuming_words:
      for to_consum, word in consuming_words[char]:
        consuming_words[char].remove((to_consum, word))
        if len(word) < len(res): continue 
        if len(to_consum) == 1 and len(word) > len(res): res = word
        else:
          if not to_consum[0] in consuming_words: consuming_words[to_consum[0]] = []
          consuming_words[to_consum[0]].append((to_consum[1:], word))
  return res

S = "abppplee"
D = [ "able", "ale", "apple", "bale", "kangaroo" ]
print(longest_word(S, D))

