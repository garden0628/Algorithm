n, m, k = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

people = []
for _ in range(m):
    x, y = map(int, input().split())
    people.append([x-1, y-1])

x, y = map(int, input().split())
exit = [x-1, y-1]

# 상 하 좌 우 순서대로 움직이기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def calculate_distance(x, y):
    return abs(x - exit[0]) + abs(y - exit[1])

def person_move(pos):
    cur_x, cur_y = pos[0], pos[1]
    cur_distance = calculate_distance(cur_x, cur_y)

    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]
        if (0 <= next_x < n) and (0 <= next_y < n):
            if maze[next_x][next_y] == 0:
                if cur_distance > calculate_distance(next_x, next_y):
                    return [next_x, next_y]
    return [cur_x, cur_y]


def is_correct_square(x, y, l):
    global people

    isPeople, isExit = False, False
    for i in range(x, x+l):
        for j in range(y, y+l):
            if [i, j] in people: isPeople = True
            elif [i, j] == exit: isExit = True
    if isPeople and isExit: return True
    return False


def find_smallest_square():
    for i in range(2, n+1):
        for j in range(n-i+1):
            for k in range(n-i+1):
                if is_correct_square(j, k, i):
                    return ([j, k], i)


def rotate_square(pos, length):
    global maze, exit, people

    x, y = pos[0], pos[1]
    previous = [[0]*length for _ in range(length)]

    for i in range(y, y+length):
        for j in range(x, x+length):
            if maze[j][i] > 0: maze[j][i] -= 1
            previous[j-x][i-y] = maze[j][i]
            
    for i in range(y+length-1, y-1, -1):
        for j in range(x, x+length):
            maze[j][i] = previous[(y+length-1)-i][j-x]

    for i in range(len(people)):
        px, py = people[i][0], people[i][1]
        if x<=px<x+length and y<=py<y+length:
            ox, oy = px-x, py-y
            rx, ry = oy, length-ox-1
            people[i] = [rx+x, ry+y]
    
    ex, ey = exit[0], exit[1]
    if x<=ex<x+length and y<=ey<y+length:
        ox, oy = ex-x, ey-y
        rx, ry = oy, length-ox-1
        exit = [rx+x, ry+y]

    
total_distance = 0
for step in range(k):
    num_of_people = len(people)

    for i in range(num_of_people):
        pos = people[i]
        if pos == [-1, -1]: continue
        next_pos = person_move(pos)

        if pos != next_pos:
            total_distance += 1
        
        if next_pos != exit:
            people[i] = next_pos
        else: people[i] = [-1, -1]
    
    cnt = people.count([-1, -1])
    if num_of_people == cnt: break

    start_pos, length = find_smallest_square()
    rotate_square(start_pos, length)


print(total_distance)
print(exit[0]+1, exit[1]+1)
