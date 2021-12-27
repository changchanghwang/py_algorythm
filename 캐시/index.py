cacheSize = 4
cities =['1','2','3','4']

from collections import deque

def solution(cacheSize, cities):
  answer = 0
  cache = deque([])
  if cacheSize ==0:
    return len(cities)*5
  for city in cities:
    city = city.lower()
    if city in cache:
      answer += 1
      cache.remove(city)
      cache.append(city)
      continue
    if not city in cache:
      answer += 5
      if len(cache) < cacheSize:
        cache.append(city)
      else:
        cache.popleft()
        cache.append(city)
  
  return answer

print(solution(cacheSize,cities))