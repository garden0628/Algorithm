from collections import deque
import sys

def dfs(v):
    count = 0
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        #print(v, end = " ")
        count += 1
        for j in range(1, com+1):
            if(visit_list[j]==0 and graph[v][j] == 1):
                q.append(j)
                visit_list[j] = 1
    print(count-1)

com = int(input())
t = int(input())

graph = [[0]*(com+1) for _ in range(com+1)]
visit_list = [0]*(com+1)

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
    
dfs(1)