import sys

while True:
  str = sys.stdin.readline().rstrip()
  if str == '.':
    break
  s = list(str)
  array1 = []
  array2 = []
  for i in s:
    if i =="(" or i==")" or i =="[" or i =="]":
      array1.append(i)
  while len(array1)>0:
    array2.append(array1.pop())
    if array2[-1] == "[" or array2[-1]=="" == array1[0]:
      array2.pop()
    if not len(array2) and len(array1):
      print('no')
      break
  if not len(array2) and not len(array1):
    print('yes')
      