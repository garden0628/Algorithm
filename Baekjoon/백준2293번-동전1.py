import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coin = []
for _ in range(n):
    coin.append(int(read()))
    
dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        if i-c>=0:
            dp[i] += dp[i-c]
            
print(dp[k])
