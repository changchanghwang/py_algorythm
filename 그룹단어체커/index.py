import sys

n = int(sys.stdin.readline())

count = n

for _ in range(n):
  word = sys.stdin.readline().rstrip()
  for i in range(len(word)-1):
    if word[i]!=word[i+1]: # 다음단어와 같지않고
      if word[i] in word[i+1:]: # 문자열의 다음에 포함되어있으면
        count-=1 # 전체갯수에 -1
        break
    
print(count)