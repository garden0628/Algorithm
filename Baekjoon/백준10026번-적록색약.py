import sys
sys.setrecursionlimit(10000)

n = int(input())

board, special_board = [], []
for _ in range(n):
    line = list(input())
    board.append(line)

    new_line = []
    for i in line:
        if i == 'G': new_line.append('R')
        else: new_line.append(i)
    special_board.append(new_line)

visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, board):
    visited[x][y] = 1
    color = board[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and color==board[nx][ny]:
            dfs(nx, ny, board)


normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i, j, board)
            normal += 1

special = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i, j, special_board)
            special += 1

print(normal, special)
