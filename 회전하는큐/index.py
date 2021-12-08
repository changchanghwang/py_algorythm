import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))

array = deque([i for i in range(1,n+1)])

count = 0

for i in range(len(list)):
  if array.index(list[i]) <= len(array)//2:
    while array[0] != list[i]:
      count+=1
      array.append(array.popleft())
  else:
    while array[0] != list[i]:
      count+=1
      array.appendleft(array.pop())
  array.popleft()
  
print(count)