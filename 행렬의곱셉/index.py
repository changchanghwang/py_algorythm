arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

import numpy

def solution(arr1, arr2):
  answer = [[]]
  arr1 = numpy.array(arr1)
  arr2 = numpy.array(arr2)
  dot = numpy.dot(arr1,arr2)
  answer = dot.tolist()
  
  return answer

print(solution(arr1,arr2))