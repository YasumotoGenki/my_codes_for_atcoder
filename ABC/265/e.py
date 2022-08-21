n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
xy = dict()
for i in range(m):
    x, y = map(int, input().split())
    if x not in xy:
        xy[x] = set()
        xy[x].add(y)
    else:
        xy[x].add(y)

dp = [[[0 for _ in range(n + 1)] for __ in range(n + 1)] for ___ in range(n + 1)]
dp[0][0][0] = 1
ans = 0
mod = 998244353

for i in range(n + 1):
    for j in range(n - i + 1):
        for k in range(n - i - j + 1):
            x = a * i + c * j + e * k
            y = b * i + d * j + f * k
            if i > 0 and dp[i - 1][j][k] and (x not in xy or y not in xy[x]):
                dp[i][j][k] += dp[i - 1][j][k]
                dp[i][j][k] %= mod
            if j > 0 and dp[i][j - 1][k] and (x not in xy or y not in xy[x]):
                dp[i][j][k] += dp[i][j - 1][k]
                dp[i][j][k] %= mod
            if k > 0 and dp[i][j][k - 1] and (x not in xy or y not in xy[x]):
                dp[i][j][k] += dp[i][j][k - 1]
                dp[i][j][k] %= mod
            if i + j + k == n:
                ans += dp[i][j][k]
                ans %= mod
print(ans)