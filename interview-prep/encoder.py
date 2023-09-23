
# Write a function that replaces the words in `raw` with the words in `code_words`
# such that the first occurrence of each word in `raw` is assigned the first unassigned word in `code_words`.

# encoder(["a"], ["1", "2", "3", "4"]) → ["1"]
# encoder(["a", "b"], ["1", "2", "3", "4"]) → ["1", "2"]
# encoder(["a", "b", "a"], ["1", "2", "3", "4"]) → ["1", "2", "1"]

def encoder(raw, code):
  res = []
  _transfor = {}
  for i in range(len(raw)):
    word = raw[i]
    if not word in _transfor: _transfor[word] = code[i]
    res.append(_transfor[word])
  return res

print(encoder(["a"], ["1", "2", "3", "4"]))
print(encoder(["a", "b"], ["1", "2", "3", "4"]))
print(encoder(["a", "b", "a"], ["1", "2", "3", "4"]))