import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k


while start <= end:
  mid = (start+end)//2
  count = 0
  for i in range(1, n+1):
    count += min(n, mid//i)
    
  if count < k:
    start = mid+1
  else:
    answer = mid
    end = mid-1

print(answer)

# 각 행은 구구단처럼 1단,2단,3단 식으로 나타나기때문에 a/행번호 가 그 행에서 구하고자 하는 개수.
# 단 a/행번호가 n보다 클 경우 n
