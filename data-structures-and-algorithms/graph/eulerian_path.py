# path in a graph that visits every edge ( -> ) exactly once

# O(E), where E is the number of edges in the graph

def is_eulerian(graph):
  # Count the number of vertices with odd degrees
  odd_count = sum(len(adj_list) % 2 != 0 for adj_list in connected_nodes(graph))

  # For an Eulerian path, there should be either 0 or 2 vertices with odd degrees
  return odd_count == 0 or odd_count == 2

def dfs(graph, u, path):
  for v in graph[u]:
    if graph[u]:  # If the edge u -> v is not removed yet
      graph[u].remove(v)
      graph[v].remove(u)
      dfs(graph, v, path)
  path.append(u)

def eulerian_path(graph, nodes):
  if not is_eulerian(graph): return None

  # Find a starting vertex with an odd degree (if any)
  start_vertex = next((v for v in nodes if len(graph[v]) % 2 != 0), next(iter(nodes)))

  path = []
  dfs(graph, start_vertex, path)
  return path[::-1]  # Reverse the path to get the correct order