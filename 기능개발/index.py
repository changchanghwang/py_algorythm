from collections import deque

progresses = [40, 93, 30, 55, 60, 65]
speeds =  [60, 1, 30, 5, 10, 7]

def solution(progresses, speeds):
  answer = []
  speeds = deque(speeds)
  p = deque([x+y for x,y in zip(progresses,speeds)])
  while p:
    print(p)
    count = 0
    if p[0] >= 100:
      while p and p[0] >= 100:
        p.popleft()
        speeds.popleft()
        count += 1
      answer.append(count)
    p = deque([x+y for x,y in zip(p,speeds)])
    
  return answer

print(solution(progresses,speeds))