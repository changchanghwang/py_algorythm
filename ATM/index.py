import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

list =[]
for i in range(0,n):
  list.append((i+1, m[i]))
  
list.sort(key= lambda x:x[1])

answer = 0
for i in range(1,len(list)+1):
  for j in range(i):
    answer += list[j][1]
    
print(answer)