scoville = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k = 100
import heapq

def solution(scoville, k):
  answer = 0
  heapq.heapify(scoville)
  while scoville[0]<k:
    if len(scoville)<2:
      return -1
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    c = a+(b*2)
    heapq.heappush(scoville,c)
    answer+=1
  return answer

print(solution(scoville,k))