import sys

n = int(sys.stdin.readline())

remain = 1000-n

money = [1,5,10,50,100,500]

count =0

while remain!=0:
  if remain >= money[-1]:
    remain -= money[-1]
    count +=1
  else:
    money.pop()
    
print(count)