from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
magic = [list(map(int, input().split())) for _ in range(m)]

shark_x, shark_y = n//2, n//2
answer = [0, 0, 0]

def destroy(d, s):
    global board
    magic_mx = [0, -1, 1, 0, 0]
    magic_my = [0, 0, 0, -1, 1]

    shark_locx, shark_locy = n//2, n//2
    for _ in range(s):
        shark_locx += magic_mx[d]
        shark_locy += magic_my[d]
        board[shark_locx][shark_locy] = 0

def boardToLine():
    global board
    shark_locx, shark_locy = n // 2, n // 2
    line = deque()

    def putLine(x, y):
        if 0<=x<n and 0<=y<n and board[x][y]!=0:
            line.append(board[x][y])
            board[x][y] = 0

    for l in range(1, n+1):
        if l%2:
            for m in range(l):
                shark_locy -= 1
                putLine(shark_locx, shark_locy)
            for m in range(l):
                shark_locx += 1
                putLine(shark_locx, shark_locy)
        else:
            for m in range(l):
                shark_locy += 1
                putLine(shark_locx, shark_locy)
            for m in range(l):
                shark_locx -= 1
                putLine(shark_locx, shark_locy)

    return line

def destroy2():
    global answer, ball_list

    cnt_dup = 0
    while True:
        blast = deque()
        prev_ball, cur_ball = 0, 0

        cnt_num = [0, 0, 0, 0]
        for j in range(len(ball_list)):
            cur_ball = ball_list.popleft()
            cnt_num[cur_ball] += 1

            if prev_ball == cur_ball:
                blast.append(cur_ball)
            else:
                if cnt_num[prev_ball] >= 4:
                    cnt_dup += 1
                    answer[prev_ball - 1] += cnt_num[prev_ball]
                    for k in range(cnt_num[prev_ball]):
                        blast.pop()
                cnt_num[prev_ball] = 0
                blast.append(cur_ball)

            prev_ball = cur_ball

        if cnt_num[prev_ball] >= 4:
            cnt_dup += 1
            answer[prev_ball - 1] += cnt_num[prev_ball]
            for k in range(cnt_num[prev_ball]):
                blast.pop()
            cnt_num[prev_ball] = 0

        ball_list = blast
        if cnt_dup == 0: break
        else: cnt_dup = 0
    return ball_list


def changing():
    global ball_list
    after_move = deque()

    if len(ball_list) > 0:
        after_move = deque()
        prev_ball, cur_ball = ball_list.popleft(), 0
        cnt = 1
        for j in range(len(ball_list)):
            cur_ball = ball_list.popleft()
            if cur_ball == prev_ball:
                cnt += 1
            else:
                after_move.append(cnt)
                after_move.append(prev_ball)
                cnt = 1
            prev_ball = cur_ball
        after_move.append(cnt)
        after_move.append(cur_ball)
    return after_move

def lineToBoard():
    global board, ball_list
    shark_locx, shark_locy = n//2, n//2

    def putBoard(x, y):
        if 0<=x<n and 0<=y<n and len(ball_list)>0:
            board[x][y] = ball_list.popleft()

    if len(ball_list) > 0:
        for l in range(1, n+1):
            if l%2:
                for m in range(l):
                    shark_locy -= 1
                    putBoard(shark_locx, shark_locy)
                for m in range(l):
                    shark_locx += 1
                    putBoard(shark_locx, shark_locy)
            else:
                for m in range(l):
                    shark_locy += 1
                    putBoard(shark_locx, shark_locy)
                for m in range(l):
                    shark_locx -= 1
                    putBoard(shark_locx, shark_locy)


for i in range(m):
    d, s = magic.pop(0)
    destroy(d, s)

    ball_list = boardToLine()
    ball_list = destroy2()
    ball_list = changing()

    if len(ball_list) > n*n-1:
        for _ in range(len(ball_list) - (n*n-1)):
            ball_list.pop()

    lineToBoard()

result = answer[0] + 2*answer[1] + 3*answer[2]
print(result)
