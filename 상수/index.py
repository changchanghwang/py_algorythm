import sys

a,b = map(str, sys.stdin.readline().split())

a = ''.join(reversed(a))
b = ''.join(reversed(b))

print(a if int(a)>int(b) else b)