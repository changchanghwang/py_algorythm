from collections import deque

progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
  answer = []
  p = deque([x+y for x,y in zip(progresses,speeds)])
  while p:
    count = 0
    if p[0] >= 100:
      while p[0] >= 100:
        p.popleft()
        count += 1
      answer.append(count)
    p = deque([x+y for x,y in zip(p,speeds)])
    
  return answer

print(solution(progresses,speeds))