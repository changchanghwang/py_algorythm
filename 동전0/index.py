import sys

n, k = map(int, sys.stdin.readline().split())
list = []
for _ in range(n):
  coin = int(sys.stdin.readline())
  if coin <= k:
    list.append(coin)

print(coin)
count =0
while k != 0:
  count += (k//list[-1])
  if list[-1] <= k: 
    k = k % list[-1]
  else:
    list.pop()

print(count)
  