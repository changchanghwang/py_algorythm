arr = [10]
divisor = 3

def solution(arr, divisor):
    answer = []
    for num in arr:
      if num % divisor == 0:
        answer.append(num)
    return sorted(answer) or [-1] #빈 배열은 false
  
print(solution(arr,divisor))

def solution(arr, divisor):
  answer = []
  for num in arr:
    if num % divisor == 0:
      answer.append(num)
  return sorted(answer) or [-1] #빈 배열은 false