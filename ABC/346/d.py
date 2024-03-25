n = int(input())
s = input()
c = list(map(int, input().split()))

INF = 10 ** 20
# dp[現在マス][連続した文字列がすでに登場したかどうか][最後の文字] = 最小コスト
dp = [[[INF, INF] for _ in range(2)] for _ in range(n)]

if s[0] == "0":
    dp[0][0][0] = 0
    dp[0][0][1] = c[0]
else:
    dp[0][0][1] = 0
    dp[0][0][0] = c[0]

for i in range(1, n):
    if s[i] == "0":
        # コストを払って現在文字を変える場合
        # 前の文字と同じ文字に変える場合
        dp[i][1][1] = min(dp[i][1][1], dp[i - 1][0][1] + c[i])
        # 前の文字とは異なる文字に変える場合
        dp[i][1][1] = min(dp[i][1][1], dp[i - 1][1][0] + c[i])
        dp[i][0][1] = min(dp[i][0][1], dp[i - 1][0][0] + c[i])

        # そのままの場合
        dp[i][1][0] = min(dp[i][1][0], dp[i - 1][1][1], dp[i - 1][0][0])
        dp[i][0][0] = min(dp[i][0][0], dp[i - 1][0][1])

    else:
        # 前の文字と同じ文字に変える場合
        dp[i][1][0] = min(dp[i][1][0], dp[i - 1][0][0] + c[i])
        # 前の文字とは異なる文字に変える場合
        dp[i][1][0] = min(dp[i][1][0], dp[i - 1][1][1] + c[i])
        dp[i][0][0] = min(dp[i][0][0], dp[i - 1][0][1] + c[i])

        # そのままの場合
        dp[i][1][1] = min(dp[i][1][1], dp[i - 1][1][0], dp[i - 1][0][1])
        dp[i][0][1] = min(dp[i][0][1], dp[i - 1][0][0])

print(min(dp[-1][1]))