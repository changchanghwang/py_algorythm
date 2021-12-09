import sys

n = sys.stdin.readline().rstrip()

# n = x + x//100+ (x%100)//10 + (x%100)%10

list = []
length = len(n)
minnum = int(n)-(9*length)
if length <=2:
  minnum = 1
for i in range(minnum,int(n)):
  a = i
  for j in range(len(str(i))):
    a += int(str(i)[j])
  if int(n) == a:
    list.append(i)

print(min(list) if list else 0)

