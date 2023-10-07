from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
distance = [0]*100001
    
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x==k:
        print(distance[x])
        break
    
    if (0<=x-1<=100000) and (distance[x-1]==0):
        distance[x-1] = distance[x]+1
        q.append(x-1)
    if (0<=x+1<=100000) and (distance[x+1]==0):
        distance[x+1] = distance[x]+1
        q.append(x+1)
    if (0<=x*2<=100000) and (distance[x*2]==0):
        distance[x*2] = distance[x]+1
        q.append(x*2)