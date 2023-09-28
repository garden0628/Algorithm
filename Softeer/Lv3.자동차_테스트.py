import sys

n, q = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))
cost.sort()

value = [0] * len(cost)
idx = dict()
for i in range(len(cost)):
    value[i] = i * (len(cost)-i-1)
    idx[cost[i]] = i

cost = set(cost)
for _ in range(q):
    num = int(sys.stdin.readline())
    if num not in cost:
        print(0)
    else:
        print(value[idx[num]])
