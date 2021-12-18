from itertools import combinations
import sys

n,m = map(int,sys.stdin.readline().split())

L = [i for i in range(1,n+1)]

perList = list(combinations(L,m))

for i in perList:
  for j in i:
    print(j, end=' ')
  print()