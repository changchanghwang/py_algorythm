import sys
from collections import Counter

n = int(sys.stdin.readline())

list = [int(sys.stdin.readline()) for i in range(n)]

print(round(sum(list)/n))
list.sort()
print(list[n//2])

common = Counter(list).most_common(2)
if len(common)>1:
  if common[0][1] ==common[1][1]:
    print(common[1][0])
  else:
    print(common[0][0])
else:
  print(common[0][0])

print(max(list)-min(list))