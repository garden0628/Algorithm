from heapq import heapify, heappush, heappop

n, m, k = map(int, input().split())
guns = [[[] for _ in range(n)] for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            heappush(guns[i][j], -nums[j])

# x, y, d, s, g
# d : 위쪽 오른쪽 아래쪽 왼쪽
player_infos= []
for i in range(m):
    x, y, d, s = map(int, input().split())
    player_infos.append([x-1, y-1, d, s, 0])
    board[x-1][y-1].append(i)
points = [0]*m

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def exist_player(pos):
    global board
    x, y = pos[0], pos[1]

    if len(board[x][y]) != 0: return True
    return False

def player_move(player):
    global guns, board, player_infos
    x, y, d = player[0], player[1], player[2]

    player_num = board[x][y].pop() 
    nx, ny = x + dx[d], y + dy[d]
    if (nx<0 or nx>=n) or (ny<0 or ny>=n):
        d = (d+2)%4
        nx, ny = x + dx[d], y + dy[d]

    player_infos[player_num][2] = d
    return [nx, ny]
    
def pickUp_gun(pos, idx):
    global guns, player_infos
    x, y = pos[0], pos[1]

    if len(guns[x][y]) != 0:
        if -guns[x][y][0] > player_infos[idx][4]:
            prev = player_infos[idx][4]
            player_infos[idx][4] = -heappop(guns[x][y])
            if prev != 0: heappush(guns[x][y], -prev)

def loser_move(pos, loser_idx):
    global board, player_infos
    x, y, d = pos[0], pos[1], player_infos[loser_idx][2]
    nx, ny = x+dx[d], y+dy[d]
    while True:
        if 0<=nx<n and 0<=ny<n and len(board[nx][ny])==0: break
        d = (d+1)%4
        nx, ny = x+dx[d], y+dy[d]

    player_infos[loser_idx][2] = d
    return [nx, ny]


def loser_action(pos, loser_idx):
    global guns, board, player_infos
    x, y = pos[0], pos[1]
    
    if player_infos[loser_idx][4] != 0:
        heappush(guns[x][y], -player_infos[loser_idx][4])
        player_infos[loser_idx][4] = 0
    new_pos = loser_move(pos, loser_idx)

    board[new_pos[0]][new_pos[1]].append(loser_idx)
    player_infos[loser_idx][0], player_infos[loser_idx][1] = new_pos[0], new_pos[1]
    pickUp_gun(new_pos, loser_idx)

def fight(pos, idx):
    global board, player_infos
    x, y = pos[0], pos[1]
    
    s1, g1 = player_infos[idx][3], player_infos[idx][4]
    p2_num = board[x][y].pop()
    s2, g2 = player_infos[p2_num][3], player_infos[p2_num][4]
    
    if s1+g1 > s2+g2: winner, loser = idx, p2_num
    elif s1+g1 == s2+g2:
        if s1 > s2: winner, loser = idx, p2_num
        else: winner, loser = p2_num, idx
    else: winner, loser = p2_num, idx

    board[x][y].append(winner)
    player_infos[winner][0], player_infos[winner][1] = x, y
    points[winner] += abs((s1+g1) - (s2+g2))
    loser_action(pos, loser)
    pickUp_gun(pos, winner)

for _ in range(k):
    for i in range(len(player_infos)):
        new_pos = player_move(player_infos[i])
        if not exist_player(new_pos):
            player_infos[i][0], player_infos[i][1] = new_pos[0], new_pos[1]
            board[new_pos[0]][new_pos[1]].append(i)
            pickUp_gun(new_pos, i)
        else: fight(new_pos, i)

for pt in points:
    print(pt, end = " ")
