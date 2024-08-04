n = int(input())
s = input()

dp = [[0 for _ in range(3)] for _ in range(n + 1)]

for i in range(n):
    aoki_hand = s[i]
    for j, takahashi_hand in enumerate(["R", "P", "S"]):
        if takahashi_hand == "R":
            if aoki_hand == "P":
                continue
            elif aoki_hand == "R":
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j - 2])
            else:
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j - 2]) + 1
        elif takahashi_hand == "P":
            if aoki_hand == "S":
                continue
            elif aoki_hand == "P":
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j - 2])
            else:
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j - 2]) + 1
        elif takahashi_hand == "S":
            if aoki_hand == "R":
                continue
            elif aoki_hand == "S":
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j - 2])
            else:
                dp[i + 1][j] = max(dp[i][j - 1], dp[i][j - 2]) + 1

print(max(dp[-1]))