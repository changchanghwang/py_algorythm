numbers = [2,1,3,4,1]

def solution(numbers):
  answer = []
  for i in range(0,len(numbers)):
    a = numbers[i]
    for j in range(i+1,len(numbers)):
      answer.append(a + numbers[j])
  return sorted(list(set(answer)))
  
  
print(solution(numbers))