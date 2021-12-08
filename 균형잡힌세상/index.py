import sys

while True:
  array= []
  str = sys.stdin.readline().rstrip()
  if str == '.':
    break
  for i in str:
    if i == "(" or i == "[":
      array.append(i)
    elif i == ")":
      if len(array) and array[-1] == "(":
        array.pop()
      else:
        array.append(i)
    elif i == "]":
      if len(array) and array[-1] == "[":
        array.pop()
      else:
        array.append(i)
  print('no') if len(array) else print('yes')