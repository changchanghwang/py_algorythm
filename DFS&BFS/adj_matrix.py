INF = 999999999 # 무한의 비용 선언 # 2차원 리스트를 이용해 인접 행렬 표현 
graph = [ 
  [0, 7, 5], 
  [7, 0, INF], 
  [5, INF, 0] 
]   

print(graph)


n = 3
m = 2
graph = [[] for _ in range(n+1)]
for _ in range(m):
  v1, v2 = 1,2
  graph[v1].append(v2)
  graph[v2].append(v1)

visited = [False] * (n+1)

print(graph)