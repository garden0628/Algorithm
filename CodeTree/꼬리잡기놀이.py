n, m, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

points, ball_turn, step = 0, 0, 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def find_head_people():
    global board
    head_people = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: head_people.append([i, j])
    return head_people

def find_people_lines(heads):
    global board

    visit = [[False]*n for _ in range(n)]
    people_lines = []
    
    for head in heads:
        path = [head]
        while True:
            x, y = path[-1][0], path[-1][1]
            if board[x][y] == 3: break

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if ((board[nx][ny] == board[x][y]+1) or (board[nx][ny] == 2)) and not visit[nx][ny]:
                        path.append([nx, ny])
                        visit[nx][ny] = True
        
        people_lines.append(path)
    return people_lines

def head_next_step(pos):
    x, y = pos[0], pos[1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if (board[nx][ny] == 4) or (board[nx][ny] == 3): return [nx, ny]

def move_one_step(people_lines):
    global board
    for people in people_lines:
        # people[0] : head person
        prev_step = people[0]
        next_step = head_next_step(people[0])
        end_value = board[next_step[0]][next_step[1]]

        people[0] = next_step
        board[people[0][0]][people[0][1]] = 1

        for i in range(1, len(people)):
            next_step = prev_step
            if board[people[i][0]][people[i][1]] != 1:
                prev_step = people[i]
                board[next_step[0]][next_step[1]] = board[prev_step[0]][prev_step[1]]
            people[i] = next_step
        board[prev_step[0]][prev_step[1]] = end_value
    
    return people_lines

def throw_ball():
    global board, ball_turn

    if 0<=(ball_turn//n)%4<1: row, column = 0 + (ball_turn % n), 0
    elif 1<=(ball_turn//n)%4<2: row, column = n-1, 0 + (ball_turn % n)
    elif 2<=(ball_turn//n)%4<3: row, column = n-1 - (ball_turn % n), n-1
    else: row, column = 0, n-1 - (ball_turn % n)

    while (0<=row<n and 0<=column<n):
        if 1<=board[row][column]<=3: return [row, column]
        
        if 0<=(ball_turn//n)%4<1: column += 1
        elif 1<=(ball_turn//n)%4<2: row -= 1
        elif 2<=(ball_turn//n)%4<3: column -= 1
        else: row += 1

    return []

def change_front_back(people):
    global board
    front, back = people[0], people[-1]
    board[front[0]][front[1]] = 3
    board[back[0]][back[1]] = 1

def find_location(pos, people_lines):
    for people in people_lines:
        if pos in people:
            idx = people.index(pos)
            change_front_back(people)
            people.reverse()
            return idx


heads = find_head_people()
people_lines = find_people_lines(heads)

for step in range(k):
    people_lines = move_one_step(people_lines)

    hit_pos = throw_ball()
    if hit_pos != []:
        idx = find_location(hit_pos, people_lines)+1
        points += (idx**2)
    ball_turn += 1

print(points)
