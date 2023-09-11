# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

def is_same_tree(p, q):
  if q == None and p == None: return True
  if p == None or q == None: return False
  if p.val != q.val: return False
  return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right) 