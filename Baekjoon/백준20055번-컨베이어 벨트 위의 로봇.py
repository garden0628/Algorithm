from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    belt = list(map(int, input().split()))

    robot = deque()
    check_robot = [0 for j in range(n)]

    cnt_zero = 0
    process = 0

    while cnt_zero < k:
        process += 1
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        tmp = [belt.pop()]
        belt = tmp + belt
        for i in range(len(robot)):
            check_robot[robot[i]] = 0
            robot[i] += 1
            check_robot[robot[i]] = 1

        if len(robot)!=0 and robot[0]>=n-1:
            check_robot[robot[0]] = 0
            robot.popleft()

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        for i in range(len(robot)):
            pos = robot[i] + 1

            if belt[pos]!=0 and check_robot[pos]==0:
                check_robot[robot[i]] = 0
                check_robot[pos] = 1
                robot[i] = pos
                belt[pos] -= 1
                if belt[pos] == 0: cnt_zero+=1

        if len(robot)!=0 and robot[0]>=n-1:
            check_robot[robot[0]] = 0
            robot.popleft()

        if belt[0] != 0:
            robot.append(0)
            check_robot[0] = 1
            belt[0] -= 1
            if belt[0] == 0:
                cnt_zero+=1

print(process)
