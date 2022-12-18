n, k, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1 for _ in range(d)] for _ in range(k + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(k, 0, -1):
        if j > i + 1:
            continue
        for idx_d in range(d):
            if dp[j - 1][idx_d] == -1:
                continue
            rem_idx = (dp[j - 1][idx_d] + a[i]) % d
            dp[j][rem_idx] = max(dp[j - 1][idx_d] + a[i], dp[j][rem_idx])

if dp[-1][0] != -1:
    print(dp[-1][0])
else:
    print(-1)