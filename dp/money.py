import sys

n,m = map(int, sys.stdin.readline().split())

list = [int(sys.stdin.readline()) for i in range(n)]

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
  for j in range(list[i], m+1):
    if d[j - list[i]] != 10001:
      d[j] = min(d[j],d[j-list[i]]+1)
if  d[m] == 10001:
  print(-1)
else:
  print(d[m])



