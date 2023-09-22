
# The classic word-count algorithm: given an array of strings,
# return a Map<String, Integer> with a key for each different string,
# with the value the number of times that string appears in the array.

# word_count(["a", "b", "a", "c", "b"]) → {"a": 2, "b": 2, "c": 1}
# word_count(["c", "b", "a"]) → {"a": 1, "b": 1, "c": 1}
# word_count(["c", "c", "c", "c"]) → {"c": 4}

def word_count(list):
  res = {}
  for word in list:
    if not word in res: res[word] = 0

    res[word] += 1

  return res

print(word_count(["a", "b", "a", "c", "b"]))
print(word_count(["c", "b", "a"]))
print(word_count(["c", "c", "c", "c"]))