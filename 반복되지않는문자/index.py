input = "abacabade"


def find_not_repeating_character(string):
  answer = ''
  for str in string:
    if string.count(str) <2:
      answer +=str
  if answer == '':
    answer = '_'
  return answer[0]


result = find_not_repeating_character(input)
print(result)