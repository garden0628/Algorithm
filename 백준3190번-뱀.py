import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
board = [[0]*n for _ in range(n)]

k = int(read())
for _ in range(k):
    x, y = map(int, read().split())
    board[x-1][y-1] = 1

l = int(read())
snake = deque([[0, 0]])
board[0][0] = -1
ans = 0
index = 0
cur_x = 0
cur_y = 0

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
way = deque([])
for _ in range(l):
    time, rotate = read().split()
    time = int(time)
    way.append([time, rotate])

while(1):
    cur_x += dir[index][0]
    cur_y += dir[index][1]
    if(cur_x>=n or cur_x<0 or cur_y>=n or cur_y<0 or board[cur_x][cur_y]==-1):
        ans+=1
        break
    elif(board[cur_x][cur_y] == 1):
        snake.append([cur_x, cur_y])
        board[cur_x][cur_y] = -1
        ans+=1
    else:
        snake.append([cur_x, cur_y])
        board[cur_x][cur_y] = -1
        eraser = snake.popleft()
        board[eraser[0]][eraser[1]] = 0
        ans+=1
    
    if(len(way)!=0 and ans==way[0][0]):
        if(way[0][1]=='D'):
            if(index==3):
                index=0
            else:
                index+=1
        else:
            if(index==0):
                index=3
            else:
                index-=1
        way.popleft()
    
print(ans)