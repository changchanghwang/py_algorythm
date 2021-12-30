import sys

case = 0
while True:
  case+=1
  l,p,v = map(int,sys.stdin.readline().split())
  if not l and not p and not v :
    break
  date = v//p*l + min(l,v-v//p*p)
  print(f"Case {case}: {date}")
   