bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
from collections import deque

def solution(bridge_length, weight, truck_weights):
  count = 0
  trucks = deque(truck_weights)
  ing = deque([0]*bridge_length)
  while ing:
    count += 1
    ing.popleft()
    if trucks:
      if sum(ing)+trucks[0] <= weight:
        ing.append(trucks.popleft())
      else:
        ing.append(0)
      
  return count

print(solution(bridge_length,weight,truck_weights))