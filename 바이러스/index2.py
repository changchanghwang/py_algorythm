import sys
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = defaultdict(list)

for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  


visited = [False] * (n+1)
v=1

def DFS(graph,v,visited):
  visited[v]= True
  for i in graph[v]:
    if not visited[i]:
      DFS(graph,i,visited)
  return visited

print(DFS(graph,v,visited).count(True)-1)