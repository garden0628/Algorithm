import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
board = []

for i in range(0, n):
    tmp = list(map(int, read().split()))
    board.append(tmp)

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs():
    lab = []
    vir = deque([])
    for i in range(0, n):
        tmp = board[i][:]
        lab.append(tmp)
        for j in range(0, m):
            if(lab[i][j]==2):
                vir.append([i, j])
                
    while(vir):
        tmp = vir.popleft()
        vir_x = tmp[0]
        vir_y = tmp[1]

        for i in range(0, 4):
            if(0<=vir_x + dir[i][0]<n and 0<=vir_y + dir[i][1]<m):
                if(lab[vir_x + dir[i][0]][vir_y + dir[i][1]]==0):
                    lab[vir_x + dir[i][0]][vir_y + dir[i][1]]=2
                    vir.append([vir_x + dir[i][0], vir_y + dir[i][1]])
    
    cnt = 0
    for i in range(0, n):
        cnt += lab[i].count(0)
    
    global ans
    ans = max(ans, cnt)
        
    
   
def make_wall(wall):
    if(wall==3):
        bfs()
        return
    
    for i in range(0, n):
        for j in range(0, m):
            if(board[i][j]==0):
                board[i][j]=1
                make_wall(wall+1)
                board[i][j]=0
                

ans = 0
wall = 0
make_wall(wall)
print(ans)