from queue import PriorityQueue

# Find a path between two points in the
# BFS, A*

def a_star(graph, initialNode, h):
  pqueue = PriorityQueue()
  _min = float('inf')
  visited = set()
  pqueue.put( ( h(initialNode), initialNode, 1 ) ) # priority, node, time
  while not pqueue.empty():
    priority, node, time = pqueue.get_nowait()
    if h(node) == 0: # if the distance is 0
      if (time < _min): _min = min(_min, time); continue # Updates the minimum
    for target_node in graph[(node, time)]:
      if (target_node, time) not in visited:
        visited.add((target_node, time))

        pqueue.put((
          priority + h(target_node),
          target_node,
          time + 1
        ))
  return _min