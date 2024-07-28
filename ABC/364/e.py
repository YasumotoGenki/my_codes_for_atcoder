n, x, y = map(int, input().split())
list_a, list_b = [], []
for i in range(n):
    a, b = map(int,input().split())
    list_a.append(a)
    list_b.append(b)

dp = [[[10001 for _ in range(x + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(n):
    sweet = list_a[i]
    salt = list_b[i]
    for j in range(n):
        for k in range(x + 1):
            dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])
            if dp[i][j][k] < 10001:
                if k + sweet <= x:
                    dp[i + 1][j + 1][k + sweet] = min(dp[i][j][k] + salt, dp[i + 1][j + 1][k + sweet])

ans = 1
for j in range(n, -1, -1):
    for k in range(x + 1):
        if dp[-1][j][k] <= y:
            print(min(j + 1, n))
            exit()
