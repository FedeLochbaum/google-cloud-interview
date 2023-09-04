# Unlike the trees where the maximum count of edges is N - 1, the graphs support all possible conections between nodes

# G = (V, E) ( V = Nodes, E = Conections between nodes )

# There is two kind of edges, DIRECTED and UNDIRECTED
  # (u, v) -> u => v (DIRECTED), u <=> v (UNDIRECTED)

# Web crawling -> Graph Traversal

# Weighted vs Unweighted graphs ( means that the edges have or not a weight associated to each connection )

class AdjacencyListGraph: # 
  def __init__(self, edges, n):
    self.list = [[] for _ in range(n)]

    for (_from, _to) in edges:
      self.list[_from].append(_to)
      self.list[_to].append(_from)

  def adjacents(self, elem): return self.list[elem]

class AdjacencyMatrixGraph: # Efficient for dense graphs 
  def __init__(self, edges, n):
    self.matrix =[[False for _ in range(n)] for _ in range(n)]

    for (_from, _to) in edges:
      self.matrix[_from][_to] = True
      self.matrix[_to][_from] = True

  def adjacents(self, elem):
    adjs = []
    for i in range(len(self.matrix[elem])):
      if self.matrix[elem][i]: adjs.append(i)
    return adjs
