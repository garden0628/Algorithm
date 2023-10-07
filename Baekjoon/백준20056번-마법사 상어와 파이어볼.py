n, m, k = map(int, input().split())

fireballs = []
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

board = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + cs*dx[cd]) % n
        nc = (cc + cs*dy[cd]) % n
        board[nr][nc].append([cm, cs, cd])

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                sum_m, sum_s, odd, even, cnt = 0, 0, 0, 0, len(board[i][j])
                while board[i][j]:
                    bm, bs, bd = board[i][j].pop(0)
                    sum_m += bm
                    sum_s += bs
                    if bd % 2 == 0: even+=1
                    else: odd+=1

                if odd==cnt or even==cnt: nd = [0, 2, 4, 6]
                else: nd = [1, 3, 5, 7]

                if sum_m//5:
                    for d in nd:
                        fireballs.append([i, j, sum_m//5, sum_s//cnt, d])

            if len(board[i][j]) == 1:
                fireballs.append([i, j] + board[i][j].pop())

print(sum([f[2] for f in fireballs]))
