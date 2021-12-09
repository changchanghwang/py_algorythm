import sys

n = int(sys.stdin.readline())

list = []
for _ in range(n):
  a,b = map(int, sys.stdin.readline().split())
  list.append((a,b,b-a))
  
list.sort(key=lambda x: (x[0]+x[2], x[0]))

time_table = [list[0]]

for i in range(1,len(list)):
  if list[i][0]<time_table[-1][1]:
    continue
  else:
    time_table.append(list[i])

print(len(time_table))
      