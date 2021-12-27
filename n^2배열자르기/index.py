n=3
left=2
right =5

def solution(n, left, right):
  answer = []
  arr = [[col if col>row else row for col in range(1,n+1)]for row in range(1,n+1)]
  for i in range(left,right+1):
    answer.append(arr[i//n][i%n])
  return answer

def solution(n, left, right):
  answer = []
  for i in range(left,right+1):
    answer.append(max(i//n,i%n)+1)
  return answer

print(solution(n,left,right))