n = int(input())
txa = [[0 for _ in range(5)] for __ in range(10 ** 5 + 1)]
max_t = 0
for i in range(n):
    t, x, a = map(int, input().split())
    txa[t][x] += a
    max_t = t
dp = [[0 for _ in range(5)] for __ in range(10 ** 5 + 1)]

for t in range(10 ** 5 + 1):
    for x in range(5):
        if x > t:
            continue
        if t == 0:
            dp[t][x] = dp[t - 1][x] + txa[t][x]
        if t > 0:
            dp[t][x] = max(dp[t][x], dp[t - 1][x] + txa[t][x])
        if t >= 1:
            if x - 1 >= 0:
                dp[t][x] = max(dp[t][x], dp[t - 1][x - 1] + txa[t][x])
            if x + 1 <= 4:
                dp[t][x] = max(dp[t][x], dp[t - 1][x + 1] + txa[t][x])
print(max(dp[-1]))