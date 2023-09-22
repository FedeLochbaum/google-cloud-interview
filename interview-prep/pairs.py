
# Given an array of non-empty strings, create and return a Map<String,
# String> as follows: for each string add its first character as a key with its last character as the value.

# pairs(["code", "bug"]) → {"b": "g", "c": "e"}
# pairs(["man", "moon", "main"]) → {"m": "n"}
# pairs(["man", "moon", "good", "night"]) → {"g": "d", "m": "n", "n": "t"}

def pairs(list):
  res = {}
  for word in list:
    res[word[0]] = word[-1]

  return res

print(pairs(["code", "bug"]))
print(pairs(["man", "moon", "main"]))
print(pairs(["man", "moon", "good", "night"]))