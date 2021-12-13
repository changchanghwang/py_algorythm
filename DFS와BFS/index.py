import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
  v1, v2 = map(int,sys.stdin.readline().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

print(graph)

def DFS(dic,start,visited):    
  stack = [start]
  while stack:
    cur = stack.pop()
    visited.append(cur)
    for d in dic[cur]:
      if d not in visited:
        stack.append(d)
  return visited

def BFS(dic,start,visited):
  queue = deque([start])
  while queue:
    cur = queue.popleft()
    visited.append(cur)
    for d in dic[cur]:
      if d not in visited:
        queue.append(d)
  return visited 

visited = []
print(DFS(graph,v,visited))
visited = []
print(BFS(graph,v,visited))