from min_heap import *
# TODO: modify the min_heap to save pairs (weight, val) instead of just weight

class PriorityQueue:
  def __init__(self):
    self.elements = MinHeap()

  def is_empty(self):
    return self.elements.is_empty()

  def push(self, priority, item):
    self.elements.add(priority, item)

  def pop(self):
    return self.elements.pop() if not self.is_empty() else None