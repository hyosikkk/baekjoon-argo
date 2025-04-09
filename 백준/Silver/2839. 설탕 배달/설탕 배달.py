n = int(input())
INF = float('inf')

dp = [INF] * (n + 1)
dp[0] = 0  # 0kg은 봉지 0개로 가능

for i in range(1, n + 1):
    if i >= 3 and dp[i - 3] != INF:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5 and dp[i - 5] != INF:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])