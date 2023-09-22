
# Consider the leftmost and righmost appearances of some value in an array.
# We'll say that the "span" is the number of elements between the two inclusive.
# A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)

# map_span([1, 2, 1, 1, 3]) → 4
# map_span([1, 4, 2, 1, 4, 1, 4]) → 6
# map_span([1, 4, 2, 1, 4, 4, 4]) → 6

def map_span(list):
  _map = {}
  _max = 0
  for i in range(len(list)):
    elem = list[i]
    if not elem in _map: _map[elem] = i
    else: _max = max(_max, i - _map[elem] + 1)
  return _max

print(map_span([1, 2, 1, 1, 3]))
print(map_span([1, 4, 2, 1, 4, 1, 4]))
print(map_span([1, 4, 2, 1, 4, 4, 4]))