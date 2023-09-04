class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop() if not self.is_empty() else None

  def peek(self):
    return self.items[-1] if not self.is_empty() else None

  def size(self):
    return len(self.items)
  
# Other option is to implement it as linked list where the root is saved and
# each node know the inmediatly below