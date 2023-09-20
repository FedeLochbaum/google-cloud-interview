# Given three ints, a b c, one of them is small, one is medium and one is large.
# Return true if the three values are evenly spaced,
# so the difference between small and medium is the same as the difference between medium and large.

# evenlySpaced(2, 4, 6) → true
# evenlySpaced(4, 6, 2) → true
# evenlySpaced(4, 6, 3) → false

def evenly_spaced(a, b, c):
  _min, _mid, _max = sorted([a, b, c])
  return abs(_min - _mid) == abs(_max - _mid)

print(evenly_spaced(2, 4, 6))
print(evenly_spaced(4, 6, 2))
print(evenly_spaced(4, 6, 3))