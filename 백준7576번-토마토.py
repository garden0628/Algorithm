from collections import deque
import sys
read = sys.stdin.readline

m, n = map(int, read().split())
farm = []
tomato = deque()
cnt_nontomato = m*n
days = 0

for i in range(n):
    temp = list(map(int, read().split()))
    
    for j in range(len(temp)):
        if temp[j]==1:
            tomato.append([i, j])
            cnt_nontomato -= 1
        elif temp[j]==-1:
            cnt_nontomato -= 1
            
    farm.append(temp)
    
while(1):
    length = len(tomato)
    cnt = 0
    
    for _ in range(length):
        tmp = tomato.popleft()
        x = tmp[0]
        y = tmp[1]
    
        if (x-1>-1) and (farm[x-1][y]==0):
            farm[x-1][y]=1
            tomato.append([x-1, y])
            cnt_nontomato-=1
            cnt+=1
        if (x+1<n) and (farm[x+1][y]==0):
            farm[x+1][y]=1
            tomato.append([x+1, y])
            cnt_nontomato-=1
            cnt+=1
        if (y-1>-1) and (farm[x][y-1]==0):
            farm[x][y-1]=1
            tomato.append([x, y-1])
            cnt_nontomato-=1
            cnt+=1  
        if (y+1<m) and (farm[x][y+1]==0):
            farm[x][y+1]=1
            tomato.append([x, y+1])
            cnt_nontomato-=1
            cnt+=1
    
    if cnt!=0:
        days += 1
    if (cnt_nontomato==0) or (len(tomato)==0):
        break
    
if cnt_nontomato!=0:
    days = -1
print(days)