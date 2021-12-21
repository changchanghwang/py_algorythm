a = [1,4,2]
b = [5,4,4]

def solution(A,B):
  answer = 0
  A.sort()
  B.sort(key=lambda x: -x)
  for i in range(len(A)):
    answer += (A[i]*B[i])
  return answer
  
print(solution(a,b))