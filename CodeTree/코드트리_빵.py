from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

store = []
for _ in range(m):
    x, y = map(int, input().split())
    store.append([x-1, y-1])

time = 0
people = deque()
access = [[True]*n for _ in range(n)]
finish = [False]*m

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def find_basecamp(x, y):
    global access
    q = deque([[0, x, y]])
    available_basecamp = []
    visit = [[False]*n for _ in range(n)]
    visit[x][y] = True

    while q:
        cur = q.popleft()
        for i in range(4):
            step, nx, ny = cur[0], cur[1]+dx[i], cur[2]+dy[i]
            if 0<=nx<n and 0<=ny<n and access[nx][ny] and not visit[nx][ny]:
                q.append([step+1, nx, ny])
                visit[nx][ny] = True
                if board[nx][ny] == 1: available_basecamp.append([step+1, nx, ny])
    
    available_basecamp.sort()
    return [available_basecamp[0][1], available_basecamp[0][2]]

def find_path(x, y, target):
    global access
    q = deque([[[x, y]]])
    visit = [[False]*n for _ in range(n)]
    visit[x][y] = True

    while q:
        path = q.popleft()
        cur = path[-1]
        for i in range(4):
            nx, ny = cur[0]+dx[i], cur[1]+dy[i]
            if 0<=nx<n and 0<=ny<n and access[nx][ny] and not visit[nx][ny]:
                if [nx, ny] == target:
                    return path + [[nx, ny]]
                q.append(path + [[nx, ny]])
                visit[nx][ny] = True


def move(person, target):
    x, y = person[0], person[1]
    path = find_path(x, y, target)
    next_step = path[1]
    return next_step

def compare_location(people, store):
    global access
    for i in range(len(people)):
        if people[i] == store[i]:
            finish[i] = True
            access[store[i][0]][store[i][1]] = False

while True:
    time += 1

    for i in range(len(people)):
        person = people.popleft()
        if not finish[i]:
            person = move(person, store[i])
        people.append(person)
    
    compare_location(people, store)

    if finish.count(True) == m: break

    if time <= m:
        target = store[time-1]
        basecamp = find_basecamp(target[0], target[1])
        access[basecamp[0]][basecamp[1]] = False
        people.append(basecamp)

print(time)
