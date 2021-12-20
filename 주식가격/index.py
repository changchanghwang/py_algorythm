prices = [1,2,3,2,3]
from collections import deque

def solution(prices):
  answer =[]
  prices = deque(prices)
  while prices:
    price = prices.popleft()
    count =0
    for i in prices:
      count +=1
      if i < price:
        break
    answer.append(count)
  return answer

print(solution(prices))