import sys
from collections import deque
read = sys.stdin.readline

n, k = map(int, read().split())
fish = list(map(int, read().split()))

def first():
    min_fish = min(fish)
    for i in range(len(fish)):
        if(fish[i]==min_fish):
            fish[i]+=1    
    space = [fish]
    step = 0
    
    while(1):
        step+=1
        new = []
        tmp = []
        
        for _ in range(2):
            #print(space)
            for i in range(step):
                for j in range(len(space)):
                    tmp.append(space[len(space)-1-j][i])
                new.append(tmp)
                tmp = []   
            
            for i in range(step, len(space[-1])):
                tmp.append(space[-1][i])
            new.append(tmp)
            space = new
            
            if(len(space)>(len(space[-1])-step)):
                #print(space)
                return space
            
            new = []
            tmp = []
 
def make_1d(fish):
    new = []
    for i in range(len(fish[0])):
        for j in range(len(fish)):
            new.append(fish[len(fish)-1-j][i])
    for i in range(len(fish[0]), len(fish[-1])):
        new.append(fish[-1][i])
    return new
       
def move_fish(fish):
    diff = [[0]*len(fish[i]) for i in range(len(fish))]
    dir = [(0, 1), (1, 0)]
    
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            for k in range(2):
                if(0<=i+dir[k][0]<len(fish) and 0<=j+dir[k][1]<len(fish[i])):
                    d = abs(fish[i][j]-fish[i+dir[k][0]][j+dir[k][1]])//5
                    if(d > 0):
                        if(fish[i][j] > fish[i+dir[k][0]][j+dir[k][1]]):
                            diff[i][j] -= d
                            diff[i+dir[k][0]][j+dir[k][1]] += d
                        else:
                            diff[i][j] += d
                            diff[i+dir[k][0]][j+dir[k][1]] -= d
   
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            fish[i][j] += diff[i][j]
            
    fish = make_1d(fish)
    return fish

def second(fish):
    new = []
    tmp = []
    
    for i in range(n//2):
        tmp.append(fish[(n//2)-1-i])
    new.append(tmp)
    tmp = []
    for i in range(n//2, n):
        tmp.append(fish[i])
    new.append(tmp)
    fish = new
    #print(fish)
    new = []
    tmp = []
    
    for i in range(2):
        for j in range(n//4):
            tmp.append(fish[1-i][(n//4)-1-j])
        new.append(tmp)
        tmp = []
    for i in range(2):
        for j in range(n//4, n//2):
            tmp.append(fish[i][j])
        new.append(tmp)
        tmp = []
    fish = new
    
    fish = move_fish(fish)
    return fish
 
cnt = 0

while(1):
    fish = first()
    #print(cnt, fish)
    fish = move_fish(fish)
    #print(cnt, fish)
    fish = second(fish)
    #print(cnt, fish)
    cnt+=1
    #print(fish)
    if(max(fish)-min(fish)<=k):
        break
print(cnt)