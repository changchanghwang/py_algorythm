input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
  array.sort()
  answer = 0
  for num in array:
    if num <= 1 or answer <= 1:
      answer += num
    else:
      answer *= num
  return answer


result = find_max_plus_or_multiply(input)
print(result)