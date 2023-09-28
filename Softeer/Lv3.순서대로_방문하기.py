
def dfs(cur, step):
    if step == m:
        answer.append(cur)
        return

    if(cur[-1] == place[step]):
        dfs(cur, step+1)
        return

    for i in range(4):
        nx = cur[-1][0] + dx[i]
        ny = cur[-1][1] + dy[i]

        if (nx<0 or ny<0 or nx>=n or ny>=n):
            continue
        if (board[nx][ny] == 1):
            continue
        if [nx, ny] not in cur:
            dfs(cur + [[nx, ny]], step)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

place = []
for _ in range(m):
    x, y = map(int, input().split())
    place.append([x-1, y-1])

answer = []
dfs([place[0]], 0)

print(len(answer))
