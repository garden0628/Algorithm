h, w = map(int, input().split())
path = []
for _ in range(h):
    path.append(list(input()))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def find_starting_point():    
    for i in range(h):
        for j in range(w):
            if path[i][j] == '#':
                cnt = 0
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=nx<h and 0<=ny<w:
                        if path[nx][ny] == '#': cnt+=1
                if cnt == 1:
                    return [i,j]


def find_direction(point):
    # left, up, right, down
    direction = [0, 0, 0, 0]
    for i in range(4):
        nx, ny = point[0]+dx[i], point[1]+dy[i]
        if 0<=nx<h and 0<=ny<w:
            if path[nx][ny] == '#': 
                direction[i] += 1
                break
    return direction


def rotate(cur_dir, next_dir):
    global command

    cur_idx = cur_dir.index(1)
    next_idx = next_dir.index(1)
    if cur_idx == next_idx:
        return
    if abs(cur_idx-next_idx) <= 2:
        if cur_idx > next_idx:
            for _ in range(cur_idx-next_idx): command += "L"
        else:
            for _ in range(next_idx-cur_idx): command += "R"
    else:
        if cur_idx > next_idx: command += "R"
        else: command += "L"
    return
    

def move(point, direction):
    if direction[0] != 0:
        path[point[0]][point[1]-1], path[point[0]][point[1]-2] = ".", "."
        next_point = [point[0], point[1]-2]
    elif direction[1] != 0:
        path[point[0]-1][point[1]], path[point[0]-2][point[1]] = ".", "."
        next_point = [point[0]-2, point[1]]
    elif direction[2] != 0:
        path[point[0]][point[1]+1], path[point[0]][point[1]+2] = ".", "."
        next_point = [point[0], point[1]+2]
    elif direction[3] != 0:
        path[point[0]+1][point[1]], path[point[0]+2][point[1]] = ".", "."
        next_point = [point[0]+2, point[1]]
    return next_point


sp = find_starting_point()
print(sp[0]+1, sp[1]+1)
path[sp[0]][sp[1]] = "."

direction = find_direction(sp)
if direction[0] != 0: print("<")
elif direction[1] != 0: print("^")
elif direction[2] != 0: print(">")
elif direction[3] != 0: print("v")

command = ""
point = sp
while True:
    point = move(point, direction)
    command += "A"
    next_direction = find_direction(point)
    if sum(next_direction) == 0: break

    rotate(direction, next_direction)
    direction = next_direction
print(command)
