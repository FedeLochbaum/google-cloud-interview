
# Modify and return the given map as follows: if the key "a" has a value,
# set the key "b" to have that same value. In all cases remove the key "c", leaving the rest of the map unchanged.

# map_share({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
# map_share({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
# map_share({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}

def map_share(_dict):
  if 'a' in _dict: _dict['b'] = _dict['a']
  del _dict['c']

  return _dict

print(map_share({"a": "aaa", "b": "bbb", "c": "ccc"}))
print(map_share({"b": "xyz", "c": "ccc"}))
print(map_share({"a": "aaa", "c": "meh", "d": "hi"}))