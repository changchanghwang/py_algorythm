import sys
import heapq

n = int(sys.stdin.readline())

array =[]

for _ in range(n):
  num = int(sys.stdin.readline())
  if not num:
    if not len(array):
      print(0)
    else:
      print(heapq.heappop(array)*-1)
  else:
    heapq.heappush(array,-num)
    