# Given an iterator of iterators, implement an interleaving iterator
# Background: Iterator defined

# In object-oriented programming, the iterator pattern is a design pattern in which an iterator is used to traverse a container and access the container's elements.
# The iterator pattern decouples algorithms from containers; in some cases, algorithms are necessarily container-specific and thus cannot be decoupled. This code snippet illustrates:

# Your challenge, should you choose to accept it...
# Given an iterator of iterators, implement an interleaving iterator that takes in an iterator of iterators, and emits elements from the nested iterators in interleaved order. That is, if we had the iterators i and j iterating over the elements [ia, ib, ic] and [ja, jb] respectively, the order in which your interleaving iterator should emit the elements would be [ia, ja, ib, jb, ic].

# Your interleaving iterator should implement the Iterator interface, take in the iterator of iterators in its constructor, and provide the next and hasNext methods. Assume that there are no additional methods offered by the iterator.

# Given the following three iterators put into an array of iterators…


class CachedIterator:
  __slots__ = ["_it", "_next", "_sentinel"]

  def __init__(self, it):
    self._it = iter(it)
    self._next = self._sentinel = object()

  def has_next(self):
    if self._next is not self._sentinel: return True
    try: self._next = next(self._it)
    except StopIteration: return False
    else: return True

  def __next__(self):
    if self._next is not self._sentinel:
      result = self._next
      self._next = self._sentinel
      return result
    else:
      return next(self._it)

class IF:
  def __init__(self, its):
    self.its = its
    self.next_it = 0
  
  def hasNext(self):
    for it in self.its:
      if it.has_next(): return True

    return False
  
  def next(self):
    val = None
    while(val == None):
      it = self.its[self.next_it]
      if it.has_next(): val = next(it)
      self.next_it = (self.next_it + 1) % len(self.its)

    return val

arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9]
_if = IF([CachedIterator(iter(arr1)), CachedIterator(iter(arr2)), CachedIterator(iter(arr3))])

while (_if.hasNext()):
  print(_if.next()) # 1 4 6 2 5 7 3 8 9  