import sys
input = sys.stdin.readline

n, k = map(int, input().split())
factory = list(input())

answer = 0
for i in range(len(factory)):
    if factory[i] == 'P':
        flag = 0
        for j in range(i-k, i+k+1):
            if j<0 or j==i or j>=len(factory):
                continue
            if factory[j] == 'H':
                answer += 1
                factory[j] = 'N'
                flag = 1
            if flag == 1: break

print(answer)
