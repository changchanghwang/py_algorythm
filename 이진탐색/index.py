finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16]

# 1. 최소값+최댓값//2 찾는 수가 시돗값보다 크면
# 2. 최소값 = 시도값+1, 최대값은 그대로 시도값은 최소값+최대값 //2
# 반복


def is_existing_target_number_binary(target, array):
    min = 0
    max = array[-1]
    guess = (min+max)//2
    
    while min <= max:
      print(array[guess])
      if array[guess] == target:
        return True
      elif array[guess] < target:
        min = guess+1
      else: max = guess-1
      guess = (min+max)//2
      
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)