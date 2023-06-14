n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def dfs(x, y, t):
    global answer
    if x==n-1 and y==n-1:
        answer += 1
        return

    if t==0 or t==2:
        if y+1<n and board[x][y+1]==0:
            dfs(x, y+1, 0)
    if t==1 or t==2:
        if x+1<n and board[x+1][y]==0:
            dfs(x+1, y, 1)
    if t==0 or t==1 or t==2:
        if x+1<n and y+1<n:
            if board[x+1][y]==0 and board[x][y+1]==0 and board[x+1][y+1]==0:
                dfs(x+1, y+1, 2)

# 가로 : 0, 세로 : 1, 대각선 : 2
answer = 0
dfs(0, 1, 0)
print(answer)
