import sys

T = int(sys.stdin.readline())

def factorial(a):
  result =1;
  for i in range(1,a+1):
    result *= i
  return result

for _ in range(T):
  n,m = map(int, sys.stdin.readline().split())
  print(factorial(m)//(factorial(m-n)*factorial(n)))