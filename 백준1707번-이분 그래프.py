from collections import deque

k = int(input())

def bfs(start, group):
    queue = deque([start])
    visited[start] = group

    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = -visited[node]
            elif visited[next] == visited[node]:
                return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    visited = [False] * (v+1)

    for i in range(e):
        d1, d2 = map(int, input().split())
        graph[d1].append(d2)
        graph[d2].append(d1)

    for i in range(1, v+1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")
