import heapq

class PriorityQueue:
  def __init__(self):
    self.elements = []

  def is_empty(self):
    return len(self.elements) == 0

  def push(self, priority, item):
    heapq.heappush(self.elements, (priority, item))

  def pop(self):
    return heapq.heappop(self.elements)[1] if not self.is_empty() else None