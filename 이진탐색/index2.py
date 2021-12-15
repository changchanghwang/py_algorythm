finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
  numbers.sort()
  min = 0
  max = len(numbers)-1
  guess = (min+max)//2
  
  while min <= max:
    if numbers[guess] == target:
      return True
    elif numbers[guess] < target:
      min = guess+1
    else:
      max = guess-1
    guess = (min+max)//2
  return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)