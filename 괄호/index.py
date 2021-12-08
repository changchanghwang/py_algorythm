import sys

n = int(sys.stdin.readline())


for _ in range(n):
  array=[]
  ps = sys.stdin.readline().rstrip()
  for i in ps:
    if i == "(":
      array.append(i)
    elif len(array) and array[-1] =="(":
      array.pop()
    else:
      array.append(i)
  print('YES') if not len(array) else print('NO')
    