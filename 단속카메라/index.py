routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
from collections import deque

def solution(routes):
  routes.sort(key=lambda x: (x[1]))
  routes = deque(routes)
  stack = []
  while routes:
    r = routes.popleft()
    stack.append(r[1])
    while routes and stack[-1] >= routes[0][0]:
      routes.popleft()
  return len(stack)

print(solution(routes))

