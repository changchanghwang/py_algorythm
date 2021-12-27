n  = 5

def solution(n):
  answer = 0
  while n > 0:
    location = n//2
    rest = n%2
    n = location
    if rest !=0:
      answer +=1
  
  return answer

print(solution(n))