s = "pPoooyY"

def solution(s):
    pCnt = 0
    yCnt = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pCnt += 1
        elif s[i] == 'y' or s[i] == 'Y':
            yCnt += 1
    if pCnt == yCnt:
        return True
    else:
        return False
      
print(solution(s))

def solution(s):
  s = s.lower()
  return s.count('p') == s.count('y') #문자열 내 있는 수 카운트