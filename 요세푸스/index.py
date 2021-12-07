import sys

n, k = map(int, sys.stdin.readline().split())
array=[]
josep = []

k -= 1
a = k

for i in range(1,n+1):
  array.append(i)
  
while len(array)>0:
  while k >= len(array):
    k = k- len(array)
  josep.append(str(array.pop(k)))
  k += a

print("<"+", ".join(josep)+">")