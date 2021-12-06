n = int(input())  
st = str(n)
if n <10:
  st = '0'+str(n)
a = st[0]
b = st[-1]
count=0
  

while True:
  c = int(a)+int(b)
  a = b
  b = str(c)[-1]
  count += 1
  num = int(a+b)
  if num == n:
    break
print(count)