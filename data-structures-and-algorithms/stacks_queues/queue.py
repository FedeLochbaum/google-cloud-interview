class Queue:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0) if not self.is_empty() else None

  def first(self):
    return self.items[0] if not self.is_empty() else None

  def size(self):
    return len(self.items)

# Other option is to implement it as a double linked list with a pointer to last or
# using two stacks where is amortized time O(1) in enqueue y dequeue ( worse case O(n) )