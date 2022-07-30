import sys
import heapq
read = sys.stdin.readline

n = int(read())

heap = []
for _ in range(n):
    card = int(read())
    heapq.heappush(heap, card)
    
result = 0
while(len(heap)>1):
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    new = first+second
    result += new
    heapq.heappush(heap, new)
print(result)