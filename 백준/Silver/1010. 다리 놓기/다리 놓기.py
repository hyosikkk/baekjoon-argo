def combination_dp(n, r):
    dp = [[0] * (r+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, r)+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n][r]

t = int(input())  # 테스트 케이스 수

for _ in range(t):
    a, b = map(int, input().split())
    print(combination_dp(b, a))