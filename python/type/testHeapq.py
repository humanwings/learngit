import heapq

data = [43, 31,8,24,135,81]

heap = []

print(type(heap))

heapq.heappush(heap, 22)

heapq.heappush(heap, 16)

heapq.heappush(heap, 101)

print(type(heap))

print(len(heap))

print(heap[0])

for value in data:
    heapq.heappush(heap, value)

print(heap[0])

print(heapq.nlargest(3, heap))

print(heapq.nsmallest(3, heap))

print([heapq.heappop(heap) for i in range(len(heap))])

