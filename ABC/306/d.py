n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

INF = -(10 ** 20)
dp = [[INF for _ in range(2)] for _ in range(n + 1)]
dp[0][0] = 0
# dp[n食目][お腹の状態]
for i in range(n):
    if xy[i][0] == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + xy[i][1], dp[i][1] + xy[i][1])
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + xy[i][1])

print(max(dp[-1]))

