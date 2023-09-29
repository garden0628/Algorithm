import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    start, end = map(int, input().split())
    heappush(heap, (end, start))

answer, prev_end = 0, 0
while heap:
    end, start = heappop(heap)
    if start >= prev_end:
        answer += 1
        prev_end = end

print(answer)
