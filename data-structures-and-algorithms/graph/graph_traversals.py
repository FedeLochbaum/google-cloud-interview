from stacks_queues.stack import *
from stacks_queues.queue import *

# Graph traversal
  # BFS -> queue ( search by levels )
    # -> When you want to know if there is a path, finding hops, levels away of or distance out, garbage collection
    # Finding the shortest path, Web crawler, Finding nodes in any connected component of a graph
  # DFS -> stack ( search by leaves )
    # -> When you need to get all the posibilities, backtracking, complete search, exhausting possible paths

# O( V + E )
# Pre order traversal

def dfs(graph, initial_node): # Note: Requires less memory space
  visited = set()

  to_visit = Stack()
  to_visit.push(initial_node)

  while (not to_visit.is_empty()):
    curr = to_visit.pop()

    if (not curr in visited): visited.add(curr); print(curr)

    for next in graph.adjacents(curr):
      if (not next in visited): to_visit.push(next)

# O( V + E )
# Pre order traversal
def bfs(graph, initial_node): # Note: Requires more memory space
  visited = set()

  to_visit = Queue()
  to_visit.push(initial_node)

  while (not to_visit.is_empty()):
    curr = to_visit.pop()

    if (not curr in visited): visited.add(curr); print(curr)

    for next in graph.adjacents(curr):
      if (not next in visited): to_visit.push(next)
