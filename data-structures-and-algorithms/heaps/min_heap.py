# Complete binary tree, from left to right ( left most nodes filled )
class MinHeap:
  def __init__(self):
    self.items = []

  def is_empty(self): return len(self.items) == 0
  
  def left_child_index(self, index): return 2 * index + 1
  def right_child_index(self, index): return 2 * index + 2
  def parent_index(self, index): return int((index - 1) / 2)
  
  def has_left_child(self, index): return self.left_child_index(index) < len(self.items)
  def has_right_child(self, index): return self.right_child_index(index) < len(self.items)
  def has_parent(self, index): return self.parent_index(index) >= 0

  def left_child(self, index): return self.items[self.left_child_index(index)]
  def right_child(self, index): return self.items[self.right_child_index(index)]
  def parent(self, index): return self.items[self.parent_index(index)]

  def swap(self, i, j):
    elem = self.items[i]
    self.items[i] = self.items[j]
    self.items[j] = elem
  
  # O(1)
  def peek(self): return self.items[0] 

  # O(log n)
  def pop(self):
    elem = self.peek()
    self.items[0] = self.items[len(self.items)-1]
    self.items.pop()
    self.heapify_down()
    return elem
  
  # O(log n)
  def add(self, val):
    self.items.append(val) # inserted at the end
    self.heapify_up()
  
  def heapify_down(self):
    index = 0
    while( self.has_left_child(index) ):
      child_index = self.left_child_index(index)
      if (self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
        child_index = self.right_child_index(index)
      
      if ( self.items[child_index] < self.items[index] ):
        self.swap(index, child_index) # swap
      
      index = child_index
  
  def heapify_up(self):
    index =  len(self.items) - 1 # Last element index in the heap
    while ( self.has_parent(index) and self.parent(index) > self.items[index] ):
      # As I am less than my parent, I need to keep bubling up
      parent_index = self.parent_index(index)
      self.swap(parent_index, index)
      index = parent_index


heap = MinHeap()
heap.add(43)
heap.add(22)
heap.add(11)
heap.add(1042)
heap.add(0)

while not heap.is_empty(): print(heap.pop())