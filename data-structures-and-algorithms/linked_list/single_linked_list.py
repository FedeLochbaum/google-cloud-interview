class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.last = None
  
  # O(1)
  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.last = new_node
      return
    
    self.last.next = new_node
    self.last = new_node

  # O(1)
  def peek(self): return self.head.value

  def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  # O(n)
  def delete(self, value):
    if not self.head: return

    if self.head.value == value:
      if self.last == self.head: self.last = None
      self.head = self.head.next
      return

    current = self.head
    while current.next:
      if current.next.value == value:
        if self.last == current.next: self.last = current
        current.next = current.next.next
        return
      current = current.next

  def reverse(self):
    prev = None
    current = self.head
    self.last = current
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev