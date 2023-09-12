# Using dfs

# In the worst case, we may explore all edges, which is O(E)
# The overall time complexity of topological sort using DFS on a DAG is O(V + E)
def topological_sort_util(graph, v, visited, stack):
  visited[v] = True

  for i in graph[v]:
    if not visited[i]: topological_sort_util(graph, i, visited, stack)

  stack.insert(0, v)

def topological_sort(graph, nodes):
  visited = [False] * len(nodes)
  stack = []

  for i in range(len(nodes)):
    if not visited[i]:
      topological_sort_util(graph, i, visited, stack)

  return stack