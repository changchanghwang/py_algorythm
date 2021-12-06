N = 18

def solution(N):
  answer = 0
  while N >= 0:
    if N % 5 == 0:
      answer += N//5
      break
    else:
      N -= 3
      answer +=1
  else:
    answer = -1
      
  return answer
  
print(solution(N))