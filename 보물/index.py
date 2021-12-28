import sys

n = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A = sorted(A)
B = sorted(B,key= lambda x : -x)

S = 0
for i in range(n):
  S += (A[i]*B[i])

print(S)