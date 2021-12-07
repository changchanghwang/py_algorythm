n = int(input())

for _ in range(n):
  x,y = map(int, input().split())
  distance = y-x
  space=0 #공간이동 장치 작동 횟수
  k=0 #space 중 어디에 속하는지 알기 위한 최대 거리
  a=0.5 #거리가 두 번에 걸쳐 1씩 늘어나기 때문

  while distance > k: #거리가 최대거리보다 작아지는 순간의 space를 구하기 위함
    a += 0.5
    k += int(a)
    space += 1

  print(space)