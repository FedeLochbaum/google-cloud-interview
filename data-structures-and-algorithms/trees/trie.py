class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children: curr.children[c] = TrieNode()
      curr = curr.children[c]

    curr.is_word = True

  def search(self, word):
    curr = self.root
    for c in word:
        if c not in curr.children: return False
        curr = curr.children[c]

    return curr.is_word

  def starts_with(self, prefix):
    curr = self.root
    for c in prefix:
      if c not in curr.children: return False
      curr = curr.children[c]
    return True