n, k = map(int, input().split())
coin = sorted(set([int(input()) for _ in range(n)]))

dp = [10001] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    for c in coin:
        if i-c < 0:
            break
        else:
            dp[i] = min(dp[i-c]+1, dp[i])

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
