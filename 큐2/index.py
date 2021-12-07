import sys
from collections import deque

n = int(sys.stdin.readline())
array = deque([])

for _ in range(n):
  command = sys.stdin.readline().split()
  if command[0] == 'back':
    if len(array) ==0:
      print(-1)
    else:
      print(array[-1])
  elif command[0] == 'pop':
    if len(array) ==0:
      print(-1)
    else:
      num = array.popleft()
      print(num)
  elif command[0] == 'size':
    print(len(array))
  elif command[0] == 'empty':
    if len(array) ==0:
      print(1)
    else:
      print(0)
  elif command[0] == 'front':
    if len(array) ==0:
      print(-1)
    else:
      print(array[0])
  else:
    array.append(command[-1])