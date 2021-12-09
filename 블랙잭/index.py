import sys

n, m = map(int, sys.stdin.readline().split())

list = list(map(int,sys.stdin.readline().split()))

arr = []
for i in range(len(list)-2):
  for j in range(i+1,len(list)-1):
    for k in range(j+1,len(list)):
      arr.append(list[i]+list[j]+list[k])
  
answer = []    
for i in (set(arr)):
  if i <= m:
    answer.append(i)
    
print(max(answer))
