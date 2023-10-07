from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

move = []
for _ in range(m):
    d, s = map(int, input().split())
    move.append([d-1, s])

cloud = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])
before_cloud = [[0 for _ in range(n)] for _ in range(n)]

pos_mx = [0, -1, -1, -1, 0, 1, 1, 1]
pos_my = [-1, -1, 0, 1, 1, 1, 0, -1]

diag_x = [-1, 1, -1, 1]
diag_y = [-1, -1, 1, 1]

for i in range(m):
    for j in range(len(cloud)):
        pos_cx, pos_cy = cloud.popleft()
        d_c, s_c = move[i][0], move[i][1]
        pos_cx, pos_cy =  (pos_cx + pos_mx[d_c]*s_c)%n, (pos_cy + pos_my[d_c]*s_c)%n
        board[pos_cx][pos_cy] += 1
        cloud.append([pos_cx, pos_cy])

    for j in range(len(cloud)):
        pos_cx, pos_cy = cloud.popleft()
        before_cloud[pos_cx][pos_cy] = 1
        for k in range(4):
            pos_nx = pos_cx + diag_x[k]
            pos_ny = pos_cy + diag_y[k]
            if 0<=pos_nx<n and 0<=pos_ny<n and board[pos_nx][pos_ny]!=0:
                board[pos_cx][pos_cy] += 1

    for j in range(n):
        for k in range(n):
            if board[j][k] >= 2 and before_cloud[j][k]==0:
                cloud.append([j, k])
                board[j][k] -= 2
            if before_cloud[j][k]==1: before_cloud[j][k]=0

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]

print(answer)
