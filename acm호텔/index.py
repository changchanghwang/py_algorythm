num = int(input())
for _ in range(num):
  h,w,n = map(int, input().split())
  H = n%h #층수
  W = n//h +1 #호수
  if H == 0: #층수의 배수일때
    H = h
    W = n//h
  print(H*100 + W)