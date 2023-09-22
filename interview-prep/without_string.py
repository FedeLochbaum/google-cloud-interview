# Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive).
# You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

# without_string("Hello there", "llo") → "He there"
# without_string("Hello there", "e") → "Hllo thr"
# without_string("Hello there", "x") → "Hello there"

def without_string(base, remove):
  res = ''
  i = 0
  while(i < len(base)):
    char = base[i]
    if i + len(remove) <= len(base) and base[i:i + len(remove)] == remove: i += len(remove); continue
    res += char; i += 1
  return res

print(without_string("Hello there", "llo"))
print(without_string("Hello there", "e"))
print(without_string("Hello there", "x"))