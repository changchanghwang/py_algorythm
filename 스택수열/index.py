import sys
from collections import deque

n = int(sys.stdin.readline())

array = deque([i for i in range(1,n+1)])
stack = []
list = []

for _ in range(n):
  num = int(sys.stdin.readline())
  while array and array[0] <= num:
    stack.append(array.popleft())
    list.append('+')
  if stack and stack[-1] == num:
    stack.pop()
    list.append('-')
    
print('NO' if stack else "\n".join(list))