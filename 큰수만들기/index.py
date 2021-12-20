# number = "99991"
# number = "1231234"
number = "4177252841"
k = 4

from collections import deque

def solution(number,k):
  number = deque(list(number))
  length = len(number)-k
  stack = [number.popleft()]
  cnt = 0
  while cnt != k and number:
    n = number.popleft()
    if not stack:
      stack.append(n)
    else:
      while stack and stack[-1]<n and cnt !=k:
        stack.pop()
        cnt += 1
      stack.append(n)
  L = stack+list(number)
  if len(L) > length:
    L = L[0:length]
  return ''.join(L)
  
print(solution(number,k))