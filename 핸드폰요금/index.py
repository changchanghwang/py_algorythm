n = int(input())
times = list(map(int, input().split()))
y = 0
m = 0

for time in times:
  y += (time//30 + 1) * 10
  m += (time//60 + 1) * 15
  
if y>m:
  print('M', m)
elif y<m:
  print('Y',y)
else :
  print('Y M', y)