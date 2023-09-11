# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n,
# with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

# Example 1:

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 
# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

# Graph undireccted, connected without cycles

# def find_redundant_edges(edges):
#   n = len(edges)
#   graph = [[] for _ in range(n + 1)]

#   for u, v in edges: graph[u].append(v); graph[v].append(u) # build the graph
#   visited = set([])
#   to_visit = [1]
#   visited_edges = set([])

#   while to_visit:
#     v = to_visit.pop()
#     if v in visited: continue
#     visited.add(v);
#     for n in graph[v]:
#       if n in visited: continue # v -> n and v -> n is unnecessary
#       else:
#         if not n in to_visit:
#           visited_edges.add((v, n)); visited_edges.add((n, v))
#           to_visit.append(n)
  
#   for n in range(len(edges) - 1, -1, -1):
#     if not (edges[n][0], edges[n][1]) in visited_edges: return edges[n]

class UnionFind:
  def __init__(self, n): self.parent = list(range(n))
  
  def find(self, x):
    if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  
  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
      self.parent[root_x] = root_y

def find_redundant_edges(edges):
  n = len(edges)
  set = UnionFind(n + 1)
  redundant_edge = None

  for u, v in edges:
    if set.find(u) == set.find(v): redundant_edge = [u, v]
    else: set.union(u, v)

  return redundant_edge

print(find_redundant_edges([[1, 2],[1, 3],[2, 3]])) # [2, 3]
print(find_redundant_edges([[1,2],[2,3],[3,4],[1,4],[1,5]])) # [1, 4]
