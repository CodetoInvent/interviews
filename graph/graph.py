# graph with adjacency list

#
#          +---+
#     +---+| A |+---+
#     |    +---+    |
#   +---+         +---+
#   | B |         | C |
#   +---+         +---+
#     |    +---+    |
#     +---+| D |+---+
#          +---+
#            |
#          +---+
#          | E |
#          +---+


graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['B', 'D'],
  'D': ['B', 'C', 'E'],
  'E': ['E']
}

from collections import deque

def bfs(graph):

  queue = deque()
  visited = set()
  result = []

  root = graph.keys()[0]
  visited.add(root)
  queue.append(root)

  while queue:
    node = queue.popleft()
    result.append(node)

    for adjacent in graph[node]:
      if adjacent not in visited:
        visited.add(adjacent)
        queue.append(adjacent)

  return result

print bfs(graph)


def dfs(graph):

  stack = []
  visited = set()
  result = []

  root = graph.keys()[0]
  visited.add(root)
  stack.append(root)

  while stack:
    node = stack.pop()
    result.append(node)

    for adjacent in graph[node]:
      if adjacent not in visited:
        visited.add(adjacent)
        stack.append(adjacent)

  return result

print dfs(graph)
