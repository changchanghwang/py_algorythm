n = 78

def solution(n):
  answer = 0
  bi = bin(n)
  count = bi.count('1')
  for i in range(n+1,1000001):
    one = bin(i).count('1')
    if one == count:
      answer = i
      break
  return answer

print(solution(n))