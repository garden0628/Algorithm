import sys
read = sys.stdin.readline

m, n = map(int, read().split())

board = []
dp = []
for _ in range(m):
  board.append(list(map(int, read().split())))
  dp.append([-1 for i in range(n)])

direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(x, y):
  if x==m-1 and y==n-1:
    return 1

  if dp[x][y] != -1:
    return dp[x][y]

  cnt = 0
  for i in range(4):
    cx, cy = x+direct[i][0], y+direct[i][1]
    if 0<=cx<m and 0<=cy<n and board[x][y]>board[cx][cy]:
      cnt += dfs(cx, cy)

  dp[x][y] = cnt
  return dp[x][y]

print(dfs(0, 0))
