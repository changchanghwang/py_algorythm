import sys

n,k = map(int, sys.stdin.readline().split())

def factorial(a):
  result =1;
  for i in range(1,a+1):
    result *= i
  return result

# def fac(a):
#   if a<2:
#     return 1
#   else:
#     return a*fac(a-1)   

print(factorial(n)//(factorial(n-k)*factorial(k)))

##이항계수 (nk) = n!/(n-k)!k!