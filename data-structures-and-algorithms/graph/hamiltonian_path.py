# path that visits every vertex/node exactly once

# O(2^n), where n is the number of vertices in the graph
def is_safe(graph, v, pos, path):
  # Check if node v can be added to the path
  if graph[path[pos - 1]][v] == 0: return False

  return not v in path

def hamiltonian_util(graph, path, pos, nodes):
  if pos == len(nodes): return True  # All vertices are included in the path

  for v in range(1, len(nodes)):
    if is_safe(graph, v, pos, path):
      path[pos] = v

      if hamiltonian_util(graph, path, pos + 1): return True

      path[pos] = -1

  return False

def hamiltonian_path(graph, nodes):
  path = [-1] * len(nodes)
  path[0] = 0

  return None if not hamiltonian_util(graph, path, 1, nodes) else path