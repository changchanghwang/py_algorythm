n = 12;

def solution(n):
  answer = 0
  for num in range(1,n+1,1):
    if n % num == 0:
      answer += num
  return answer

print(solution(n))

def sumDivisor(n):
    # n // 2 의 수들만 검사하면 성능 약 2배 향상
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
  
print(sumDivisor(n))