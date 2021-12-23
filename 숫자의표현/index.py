n = 10

def solution(num):
  return len([i  for i in range(1,num+1,2) if num % i == 0])
##등차수열 합 공식

print(solution(n))