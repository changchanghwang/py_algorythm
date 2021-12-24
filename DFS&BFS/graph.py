from collections import deque

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
visited = [False]*9

def dfs(graph,start,visited):
  visited[start] = True
  print(start, end=' ')
  for node in graph[start]:
    if not visited[node]:
      dfs(graph,node,visited)
      
dfs(graph,1,visited)

print()
visited = [False]*9

def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
bfs(graph,1,visited)