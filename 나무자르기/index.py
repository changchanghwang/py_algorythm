import sys

n,m = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

trees.sort()

min = 0
max = max(trees)

while min<= max:
  guess=(min+max)//2
  optain = 0
  # for i in trees:
  #   if i >= guess:
  #     optain += (i-guess)
  optain = sum(i-guess if i>guess else 0 for i in trees)
  if optain >= m:
    min = guess +1
  else:
    max = guess -1

print(max)
