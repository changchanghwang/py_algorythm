import heapq

heap = []
heapq.heappush(heap, 50) # 힙에 원소 추가
heapq.heappush(heap, 10)
heapq.heappush(heap, 25)

result = heapq.heappop(heap) # 가장 작은 원소를 힙에서 제거 후 리턴
print(result)
print(heap)