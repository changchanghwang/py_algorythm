import sys

n = int(sys.stdin.readline())

list = sorted(list(map(int, sys.stdin.readline().split())))

print(list[0]*list[-1])