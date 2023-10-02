import itertools

def working(case):
    total_work, work, cnt, idx = 0, 0, 0, 0
    while cnt<k:
        if idx == len(case): idx = 0
        if work + case[idx] > m:
            total_work += work
            cnt += 1
            work = 0
        work += case[idx]
        idx += 1
    return total_work

n, m, k = map(int, input().split())
weight = list(map(int, input().split()))
per = itertools.permutations(weight, len(weight))

answer = 5000
for case in list(per):
    work = working(case)
    if answer > work: answer = work

print(answer)
