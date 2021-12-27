n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

from collections import deque

def bfs(arr,visited,start):
  queue = deque([start])
  visited[start] = True
  count = 1
  while queue:
    cur = queue.popleft()
    for i in arr[cur]:
      if not visited[i]:
        count +=1
        queue.append(i)
        visited[i] = True
  return count

def solution(n, wires):
  answer =n
  arr = [[]for _ in range(n+1)]
  for wire in wires:
    arr[wire[0]].append(wire[1])
    arr[wire[1]].append(wire[0])
  
  for start,not_visit in wires:
    visited = [False] *(n+1)
    visited[not_visit] = True
    result = bfs(arr,visited,start)
    if abs(result - (n-result)) < answer:
      answer = abs(result - (n-result))
  
  return answer

print(solution(n,wires))