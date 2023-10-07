from collections import deque
n, l, r = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(land, visited):
    connect = []
    while land:
        [x, y] = land.popleft()
        connect.append([x, y])

        for i in range(4):
            cx, cy = x+dx[i], y+dy[i]
            if 0<=cx<n and 0<=cy<n and visited[cx][cy]==0:
                if l<=abs(board[x][y] - board[cx][cy])<=r:
                    visited[cx][cy] = 1
                    land.append([cx, cy])
    return connect

answer = 0
while True:
    visited = [[0] * n for _ in range(n)]
    borderline = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                search = deque()
                search.append([i, j])
                borderline.append(bfs(search, visited))

    flag = 0
    for i in range(len(borderline)):
        if len(borderline[i]) > 1:
            flag = 1
            total_pop = 0
            for pos in borderline[i]:
                total_pop += board[pos[0]][pos[1]]
            pop = total_pop // len(borderline[i])
            for pos in borderline[i]:
                board[pos[0]][pos[1]] = pop

    if flag == 1:
        answer += 1
    else:
        break

print(answer)
