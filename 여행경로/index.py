from collections import defaultdict

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
  graph = defaultdict(list)
  for i in tickets:
    graph[i[0]].append(i[1])
  
  for key in graph.keys():
    graph[key].sort(reverse=True)
  stack = ['ICN']
  visited = []
  while stack:
    tmp = stack[-1] #아래서부터 채우는 로직
    if not graph[tmp]:
      visited.append(stack.pop())
    else:
      stack.append(graph[tmp].pop())
  visited.reverse() # 마지막부터 채웠기 때문에 리버스.
  return visited

print(solution(tickets))