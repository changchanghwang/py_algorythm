people = [100,500,500,900,950]
limit = 1000

from collections import deque

def solution(people, limit):
  people.sort()
  people = deque(people)
  cnt = 0
  while people:
    if len(people)>=2:
      if people[0] + people[-1] <= limit:
        people.popleft()
        people.pop()
        cnt += 1
      else:
        people.pop()
        cnt += 1
    else:
      people.pop()
      cnt+=1
  return cnt

print(solution(people,limit))