from collections import deque
from itertools import combinations
import copy

n, m, d = map(int, input().split())

board = deque()
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0, -1, 0]
dy = [-1, 0, 1]

def find_attack(x, y, board):
    queue = deque()
    queue.append((x-1, y))

    while queue:
        cx, cy = queue.popleft()
        if abs(x-cx)+abs(y-cy) > d:
            return (-1, -1)
        if board[cx][cy]==1:
            return (cx, cy)
        for i in range(3):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m:
                queue.append((nx, ny))


def after_attack(board):
    board.pop()
    board.append([0]*m)
    board.rotate(1)


nums = [i for i in range(m)]
comb = list(combinations(nums, 3))

answer = 0
attack_place = []
for case in comb:
    answer_temp = 0
    board_temp = copy.deepcopy(board)
    attacker = [(n, case[0]), (n, case[1]), (n, case[2])]

    while sum(sum(board_temp[i]) for i in range(n))!=0:
        for j in range(3):
            place = find_attack(attacker[j][0], attacker[j][1], board_temp)
            if place != (-1, -1) and place not in attack_place:
                attack_place.append(place)

        answer_temp += len(attack_place)
        # print(attack_place)
        while attack_place:
            x, y = attack_place.pop()
            board_temp[x][y] = 0

        after_attack(board_temp)
    # print(answer_temp)
    answer = max(answer, answer_temp)

print(answer)
