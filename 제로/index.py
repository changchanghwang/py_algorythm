k = int(input())
array = []
for _ in range(k):
  n = int(input())
  if n ==0:
    array.pop(-1)
  else:
    array.append(n)
print(sum(array))