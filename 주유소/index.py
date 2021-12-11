import sys

n = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))

price = list(map(int, sys.stdin.readline().split()))

sum = price[0] * distance[0]
m = price[0]

for i in range(1, n-1):
  if price[i] < m:
    sum += price[i] * distance[i]
    m = price[i]
  else:
    sum += m * distance[i]
    
print(sum)