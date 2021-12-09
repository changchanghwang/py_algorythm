import sys

s = sys.stdin.readline().rstrip()

s = s.split('-')
expression = []
for i in s:
  i = i.split('+')
  expression.append(i)

## 초기값
sum=0
for i in expression[0]:
  sum += int(i)

## 최소값을 구하는 계산식
for i in range(1,len(expression)):
  a = 0
  for j in expression[i]:
    a += int(j)
  sum -= a
print(sum)