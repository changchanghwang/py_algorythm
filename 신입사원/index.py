import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  mans = []
  count = 1
  for i in range(n):
    mans.append(list(map(int, sys.stdin.readline().split())))
  
  mans.sort()
  Max = mans[0][1]
  for i in range(1,n):
    if Max > mans[i][1]:
      count +=1 
      Max = mans[i][1]
  
  print(count)