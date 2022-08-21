n, m = map(int, input().split())
x = list(map(int, input().split()))
cy = dict()
for i in range(m):
    c, y = map(int, input().split())
    cy[c] = y

dp = [[0 for __ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if j > i:
            break
        c = 0
        if j + 1 in cy:
            c = cy[j + 1]
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i] + c)
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
print(max(dp[-1]))