from heapq import heappush, heappop
n, k = map(int, input().split())

jew = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jew.sort()
bags.sort()

answer = 0
jew_tmp = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heappush(jew_tmp, -jew[0][1])
        heappop(jew)
    if jew_tmp:
        answer -= heappop(jew_tmp)
    elif not jew:
        break

print(answer)
