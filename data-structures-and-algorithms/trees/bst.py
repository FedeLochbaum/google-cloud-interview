class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

  def insert(self, val):
    if (self.val < val): self.insert_to_right(val); return

    self.insert_to_left(val)
  
  def insert_to_right(self, val):
    if self.right == None: self.right = Node(val); return
    
    self.right.insert(val)

  def insert_to_left(self, val):
    if self.left == None: self.left = Node(val); return
  
    self.left.insert(val)

  def search(self, val):
    if self.val == val: return self

    if self.val < val: return None if self.right == None else self.right.search(val)

    return None if self.left == None else self.left.search(val)

  def delete(self, val):
    if self.val < val:
      self.right = self.right.delete(val)
    elif self.val > val:
      self.left = self.left.delete(val)
    else:
      if self.left is None: return self.right
      elif self.right is None: return self.left

      _min = self.right.min_node() # The most to the left

      self.val = _min.val

      # Delete _min
      self.right = self.right.delete(_min.val)

    return self

  def min_node(self): return self if self.left == None else self.left.min_node()

  def inorder_traversal(self):
    self.left.inorder_traversal()
    print(self.val)
    self.right.inorder_traversal()
