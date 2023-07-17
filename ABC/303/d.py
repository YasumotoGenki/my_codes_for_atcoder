x, y, z = map(int, input().split())
s = input()

inf = 10 ** 100
dp = [[inf, inf] for _ in range(len(s) + 1)]
dp[0][0] = 0

# 0-> 押してない、1-> 押している
for i, ch in enumerate(s):
    if ch == "a":
        dp[i + 1][0] = min(dp[i][0] + x, dp[i][1] + z + x)
        dp[i + 1][1] = min(dp[i][1] + y, dp[i][0] + z + y)
    else:
        dp[i + 1][0] = min(dp[i][0] + y, dp[i][1] + z + y)
        dp[i + 1][1] = min(dp[i][1] + x, dp[i][0] + z + x)

print(min(dp[-1]))