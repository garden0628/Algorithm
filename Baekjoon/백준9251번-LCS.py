import sys
read = sys.stdin.readline

first = read().strip()
second = read().strip()

w = len(first)
h = len(second)
common = [[0]*(w+1) for _ in range(h+1)]

for i in range(1, w+1):
    for j in range(1, h+1):
        if first[i-1] == second[j-1]:
            common[j][i] = common[j-1][i-1] + 1
        else:
            common[j][i] = max(common[j][i-1], common[j-1][i])
            
print(common[h][w])