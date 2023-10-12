from collections import deque

n, m, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

attacker_history = []
copy_board = [[0]*m for _ in range(n)]

def select_attacker():
    global board, attacker_history
    tower, tower_value = [-1, -1], 5001

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: continue
            if board[i][j] < tower_value:
                tower, tower_value = [i, j], board[i][j]
            elif board[i][j] == tower_value:
                if tower not in attacker_history and [i, j] not in attacker_history:
                    if i+j > tower[0]+tower[1]:
                        tower, tower_value = [i, j], board[i][j]
                    elif i+j == tower[0]+tower[1]:
                        if j > tower[1]:
                            tower, tower_value = [i, j], board[i][j]
                elif tower not in attacker_history and [i, j] in attacker_history:
                    tower, tower_value = [i, j], board[i][j]
                elif tower in attacker_history and [i, j] not in attacker_history:
                    continue
                else:
                    for idx in range(len(attacker_history)):
                        if attacker_history[idx] == tower:
                            prev_history = idx
                        if attacker_history[idx] == [i, j]:
                            cur_history = idx
                    if cur_history > prev_history:
                        tower, tower_value = [i, j], board[i][j]
    return tower

def select_strongest(attacker):
    global board, attacker_history
    tower, tower_value = [-1, -1], -1

    for i in range(n):
        for j in range(m):
            if [i, j] == attacker: continue
            if board[i][j] > tower_value:
                tower, tower_value = [i, j], board[i][j]
            elif board[i][j] == tower_value:
                if tower not in attacker_history and [i, j] not in attacker_history:
                    if i+j < tower[0]+tower[1]:
                        tower, tower_value = [i, j], board[i][j]
                    elif i+j == tower[0]+tower[1]:
                        if j < tower[1]:
                            tower, tower_value = [i, j], board[i][j]
                elif tower not in attacker_history and [i, j] in attacker_history:
                    continue
                elif tower in attacker_history and [i, j] not in attacker_history:
                    tower, tower_value = [i, j], board[i][j]
                else:
                    for idx in range(len(attacker_history)):
                        if attacker_history[idx] == tower:
                            prev_history = idx
                        if attacker_history[idx] == [i, j]:
                            cur_history = idx
                    if prev_history > cur_history:
                        tower, tower_value = [i, j], board[i][j]
    return tower

def inBoard(x, y):
    if x<0: x+=n
    elif x>=n: x-=n
    
    if y<0: y+=m
    elif y>=m: y-=m 

    return x, y

def find_path(attacker, victim):
    global board

    all_path = deque([[attacker]])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit = [[False]*m for _ in range(n)]
    visit[attacker[0]][attacker[1]] = True

    while all_path:
        path = all_path.popleft()
        cur = path[-1]
        for i in range(4):
            nx, ny = inBoard(cur[0]+dx[i], cur[1]+dy[i])
            if board[nx][ny]!=0 and [nx, ny] not in path and visit[nx][ny]==False:
                new_path = path + [[nx, ny]]
                visit[nx][ny] = True
                if [nx, ny] == victim: return new_path
                all_path.append(new_path)
                
    return []

def attack(x, y, attack_value):
    global board
    if board[x][y] > attack_value: board[x][y] -= attack_value
    else: board[x][y] = 0

def laser_attack(attacker, victim):
    global board

    path = find_path(attacker, victim)
    if path == []: return False

    attack_path = board[attacker[0]][attacker[1]] // 2
    for i in range(1, len(path)-1):
        x, y = path[i]
        attack(x, y, attack_path)

    attack(victim[0], victim[1], board[attacker[0]][attacker[1]])
    return True

def bomb_attack(attacker, victim):
    attack_victim = board[attacker[0]][attacker[1]]
    attack_around = attack_victim // 2

    x, y = victim[0], victim[1]
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = inBoard(x+i, y+j)
            if [nx, ny] == victim: attack(nx, ny, attack_victim)
            elif [nx, ny] == attacker: continue
            else: attack(nx, ny, attack_around)

def make_copy():
    global board, copy_board
    for i in range(n):
        for j in range(m):
            copy_board[i][j] = board[i][j]

def stop_condition():
    global board
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0: cnt += 1
    if cnt > 1: return True
    else: return False

for step in range(k):
    if stop_condition() == False: break

    attacker = select_attacker()
    board[attacker[0]][attacker[1]] += (m+n)
    victim = select_strongest(attacker)
    make_copy()
    if not laser_attack(attacker, victim):
        bomb_attack(attacker, victim)
    attacker_history.append(attacker)

    for i in range(n):
        for j in range(m):
            if board[i][j]!=0 and [i, j]!=attacker and board[i][j]==copy_board[i][j]:
                board[i][j] += 1

strongest_tower = select_strongest([-1, -1])
print(board[strongest_tower[0]][strongest_tower[1]])
