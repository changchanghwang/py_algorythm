s =  " adgagd 3eagdag "

def solution(s):
  s = list(s)
  for i in range(len(s)-1):
    if i == 0:
      s[i] = s[i].upper() 
    s[i+1] = s[i+1].upper() if s[i] == " " else s[i+1].lower()
  return ''.join(s)

print(solution(s))