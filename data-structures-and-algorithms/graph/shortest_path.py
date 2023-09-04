import heapq

# Finds the shortest path from a single node A to all other nodes in a the graph
# Dijkstra's algorithm does not support negative edge weights, because will keep updating minimum paths ( looping )
# O(E + V log V)
def dijkstra(graph, initial_node):
  distances = { node: float('inf') for node in graph } # Matrix of distances
  distances[initial_node] = 0
  to_visit = [ (0, initial_node) ]

  while to_visit:
    c_distance, node = heapq.heappop(to_visit)

    if c_distance > distances[node]: continue

    for neighbor, weight in graph[node].items():
      distance = c_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(to_visit, (distance, neighbor))

  return distances

# Finds the shortests path from a single node to all nodes in the graph
# The algorithm can detect cycles running E rounds, and if running a new last round reduces any distance, the graph contains a negative cycle
# O( V * E )
def bellman_ford(graph, initial_node):
  distances = { node: float('inf') for node in graph }
  distances[initial_node] = 0

  for _ in range(len(graph) - 1):
    for node in graph:
      for neighbor, weight in graph[node].items():
        if distances[node] + weight < distances[neighbor]:
          distances[neighbor] = distances[node] + weight

  # checking negative cycles
  for node in graph:
    for neighbor, weight in graph[node].items():
      if distances[node] + weight < distances[neighbor]:
        return -1 # There is a negative cycles
  return distances

# Finds shortest path between ALL node pairs of the graph
# Handles graphs with negative weights but cannot distinguish between negative weight cycles and reachable nodes
# O ( V^3 )
def floyd_warshall(graph):
  n = len(graph)
  distances = [[float('inf')] * n for _ in range(n)]

  for i in range(n): distances[i][i] = 0

  for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
      distances[node][neighbor] = weight

  for k in range(n):
    for i in range(n):
      for j in range(n):
        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

  return distances
