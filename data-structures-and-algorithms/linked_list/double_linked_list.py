class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next= None

class LinkedList:
  def __init__(self):
    self.head = None
    self.last = None
  
  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.last = new_node
      return
    
    new_node.prev = self.last
    self.last.next = new_node
    self.last = new_node

  def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

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
        current.next.next.prev = current.next
        current.next = current.next.next
        return
      current = current.next

  def reverse(self):
    it = self.last
    self.last = self.head
    self.head = it

    it.next = it.prev

    while it.prev:
      _prev = it.prev
      it.prev = it.next
      it.next = _prev

      it = it.prev

