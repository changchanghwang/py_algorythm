import sys

n = int(sys.stdin.readline())

list = [0] * 10001

for _ in range(n):
  num = int(sys.stdin.readline())
  list[num-1] += 1

for i in range(len(list)):
  for j in range(list[i]):
    print(i+1)