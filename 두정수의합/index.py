a,b = 5,3


def solution(a, b):
    A = min(a,b) #최소값
    B = max(a,b) #최대값
    return sum(range(A,B+1)) # 배열 안에 모든것을 더함, 이때 range는 A~B+1사이 수를 모두 담음.
  
print(solution(a,b))

def solution(a,b):
  return sum([i for i in range(min(a, b), max(a, b) + 1)])