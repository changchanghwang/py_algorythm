import sys

t = int(sys.stdin.readline())


def fibonacci(n,d):
  if n in d:
    return d[n]
  fibo = fibonacci(n-1,d)+fibonacci(n-2,d)
  d[n] = fibo
  return d[n]



for _ in range(t):
  d = {
    0: 0,
    1: 1,
    2: 1
  }
  n = int(sys.stdin.readline())
  if n == 0:
    print('1 0')
  else:
    print(fibonacci(n-1,d),fibonacci(n,d))
  
  