import sys
read = sys.stdin.readline

n = int(read())
block = []
for _ in range(n):
    tmp = list(map(int, read().split()))
    block.append(tmp)

def move_right(block):
    new_block = []
    tmp = -1
    for i in range(n):
        line = []
        for j in range(1, n+1):
            if(block[i][n-j]!=0 and tmp==-1):
                tmp = block[i][n-j]
            elif(block[i][n-j]!=0 and tmp!=-1 and block[i][n-j]==tmp):
                line.append(tmp*2)
                tmp = -1
            elif(block[i][n-j]!=0 and tmp!=-1 and block[i][n-j]!=tmp):
                line.append(tmp)
                tmp = block[i][n-j]
        if(tmp!=-1):
            line.append(tmp)
            tmp = -1
        for _ in range(n-len(line)):
            line.append(0)
        new_block.append(list(reversed(line)))
    return new_block
         

def move_left(block):
    new_block = []
    tmp = -1
    for i in range(n):
        line = []
        for j in range(n):
            if(block[i][j]!=0 and tmp==-1):
                tmp = block[i][j]
            elif(block[i][j]!=0 and tmp!=-1 and block[i][j]==tmp):
                line.append(tmp*2)
                tmp = -1
            elif(block[i][j]!=0 and tmp!=-1 and block[i][j]!=tmp):
                line.append(tmp)
                tmp = block[i][j]
        if(tmp!=-1):
            line.append(tmp)
            tmp = -1
        for _ in range(n-len(line)):
            line.append(0)
        new_block.append(line)
    return new_block

def move_up(block):
    new_block = [[0]*n for _ in range(n)]
    tmp = -1
    for i in range(n):
        line = []
        for j in range(n):
            if(block[j][i]!=0 and tmp==-1):
                tmp = block[j][i]
            elif(block[j][i]!=0 and tmp!=-1 and block[j][i]==tmp):
                line.append(tmp*2)
                tmp = -1
            elif(block[j][i]!=0 and tmp!=-1 and block[j][i]!=tmp):
                line.append(tmp)
                tmp = block[j][i]
        if(tmp!=-1):
            line.append(tmp)
            tmp = -1
        for j in range(len(line)):
            new_block[j][i] = line[j]
    return new_block
        
def move_down(block):
    new_block = [[0]*n for _ in range(n)]
    tmp = -1
    for i in range(n):
        line = []
        for j in range(1, n+1):
            if(block[n-j][i]!=0 and tmp==-1):
                tmp = block[n-j][i]
            elif(block[n-j][i]!=0 and tmp!=-1 and block[n-j][i]==tmp):
                line.append(tmp*2)
                tmp = -1
            elif(block[n-j][i]!=0 and tmp!=-1 and block[n-j][i]!=tmp):
                line.append(tmp)
                tmp = block[n-j][i]
        if(tmp!=-1):
            line.append(tmp)
            tmp = -1
        for j in range(len(line)):
            new_block[(n-1)-j][i] = line[j]
    return new_block

def dfs(block, cnt):
    global result
    if(cnt==5):
        for i in range(n):
            for j in range(n):
                result = max(result, block[i][j])
        return

    dfs(move_right(block), cnt+1)
    dfs(move_left(block), cnt+1)
    dfs(move_up(block), cnt+1)
    dfs(move_down(block), cnt+1)


cnt = 0
result = 0
dfs(block, cnt)
print(result)