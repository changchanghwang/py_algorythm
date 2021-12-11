import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  d= [0] * 101

  d[1] = 1
  d[2] = 1
  d[3] = 1
  d[4] = 2
  # 4번째 전 수의 합
  # d[n] = d[n-1]+d[n-3]
  
  for i in range(5,n+1):
    d[i] = d[i-1]+d[i-5]
  
  print(d[n])