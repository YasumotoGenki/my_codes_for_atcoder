n, b, k = map(int, input().split())
c = list(map(int, input().split()))

dp = [[0 for j in range(b)] for i in range(n+1)] # [桁数][余り]
dp[0][0] = 1

for i in range(n):
    for item_c in c:
        rem = (item_c * (10 ** (n - i - 1))) % b
        for j in range(b):
            pre_rem = (j + rem) % b
            dp[i + 1][j] += dp[i][pre_rem]
            dp[i + 1][j] %= 1000000007
print(dp[n][0])