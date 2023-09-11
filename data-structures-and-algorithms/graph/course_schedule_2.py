# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
# If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

# prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai

# b_i -> a_i, ex: [0, 1] -> 1 -> 0

# Return the ordering of courses you should take to finish all courses

# NOTE: basically, we have to create a graph linking b_i -> a_i, and do BFS order to find a valid path
from collections import defaultdict, deque

# Topological sort ( DAG )
def find_order(count, dependencies):
  graph = graph = defaultdict(list); needed = [0] * count; order = []

  for course, dependency in dependencies:
    graph[dependency].append(course); needed[course] += 1

  queue = deque([c for c in range(count) if needed[c] == 0]) # possible starting points

  while queue: # BFS
    course = queue.popleft()
    order.append(course)

    # Decrease the needed of neighboring courses
    for neighbor in graph[course]:
      needed[neighbor] -= 1
      if needed[neighbor] == 0: queue.append(neighbor) # Having taking course, now we add to the queue all the unlocked courses

  return order if len(order) == count else []

print(find_order(2, [[1, 0]])) # [0, 1]
print(find_order(4, [[1, 0],[2, 0],[3, 1],[3, 2]])) # [0, 2, 1, 3]
print(find_order(1, [])) # [0]


