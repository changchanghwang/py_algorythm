import sys

t = int(sys.stdin.readline())

time = [300,60,10]
count = [0,0,0]

if t % time[2]:
  print(-1)
  exit()

while t != 0:
  if t >= time[0]:
    t -= time[0]
    count[0] += 1
  elif t >= time[1]:
    t -= time[1]
    count[1] += 1
  elif t >= time[2]:
    t -= time[2]
    count[2] += 1
    
for c in count:
  print(c ,end=' ')