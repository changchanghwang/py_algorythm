import sys

n = int(sys.stdin.readline())

ropes = []

for _ in range(n):
  ropes.append(int(sys.stdin.readline()))
  
ropes.sort(reverse=True)

list = []

for num in range(n):
  list.append(ropes[num]*(num+1))

print(max(list))