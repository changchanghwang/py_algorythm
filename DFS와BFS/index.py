import sys
from collections import deque

n,m,v = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
  v1, v2 = map(int,sys.stdin.readline().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

for i in range(n+1):
  graph[i].sort()

def DFS(graph,v,visited):    
  visited[v] = True
  print(v, end= ' ')
  for i in graph[v]:
    if not visited[i]:
      DFS(graph,i,visited)

def BFS(graph,v,visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    cur = queue.popleft()
    print(cur, end= ' ')
    for i in graph[cur]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * (n+1)
DFS(graph,v,visited)
print()
visited = [False] * (n+1)
BFS(graph,v,visited)