import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())

result = -1

que = deque([(a,1)])

while que:
  i, cnt = que.popleft()
  if i == b:
    result = cnt
    break
  if i*2 <= b:
    que.append((i*2,cnt+1))
  if int(str(i)+'1') <=b:
    que.append((int(str(i)+'1'),cnt+1))
    
print(result)