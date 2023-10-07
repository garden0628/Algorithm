from collections import deque

m, n, h = map(int, input().split())

box = []
queue = deque([])

for i in range(h):
    floor = []
    for j in range(n):
        line = list(map(int, input().split()))
        for k in range(len(line)):
            if line[k] == 1:
                queue.append([i, j, k])
        floor.append(line)
    box.append(floor)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0<=nz<m and box[nx][ny][nz] == 0:
            box[nx][ny][nz] = box[x][y][z] + 1
            queue.append([nx, ny, nz])

answer = max(max(map(max, floor)) for floor in box) -1
for floor in box:
    for row in floor:
        if 0 in row:
            answer = -1
print(answer)
