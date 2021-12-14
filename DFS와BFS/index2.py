import sys
from collections import defaultdict, deque

n,m,v = map(int,sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(len(graph)):
  graph[i].sort()

def DFS(graph,v):
  stack = [v]
  visited = []
  while stack:
    cur = stack.pop()
    print(cur, end= " ")
    visited.append(cur)
    for i in graph[cur]:
      if i not in visited:
        stack.append(i)
  return visited

def BFS(graph,v):
  queue = deque([v])
  visited = []
  while queue:
    cur = queue.popleft()
    print(cur, end = " ")
    visited.append(cur)
    for i in graph[cur]:
      if i not in visited:
        queue.append(i)
  return visited

DFS(graph,v)
print()
BFS(graph,v)
