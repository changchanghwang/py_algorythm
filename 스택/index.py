import sys

n = int(sys.stdin.readline())
array=[]

for _ in range(n):
  command = sys.stdin.readline().split()
  if command[0] == 'pop':
    if len(array) ==0:
      print(-1)
    else:
      pop = array.pop(-1)
      print(pop)
  elif command[0] == 'size':
    print(len(array))
  elif command[0] == 'empty':
    if len(array) ==0:
      print(1)
    else:
      print(0)
  elif command[0] == 'top':
    if len(array) ==0:
      print(-1)
    else:
      print(array[-1])
  else:
    array.append(command[-1])
    