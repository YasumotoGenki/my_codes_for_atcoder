n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[None for _ in range(m + 1)] for __ in range(n)]
mdp = [None for _ in range(m + 1)]
mdp[0] = 0

for i in range(n):
    for j in range(min(i + 1, m), 0, -1):
        if dp[i][j] is None:
            dp[i][j] = mdp[j - 1] + a[i] * j
        else:
            dp[i][j] = max(dp[i][j], mdp[j - 1] + a[i] * j)
        if mdp[j] is None:
            mdp[j] = dp[i][j]
        else:
            mdp[j] = max(mdp[j], dp[i][j])
    
print(mdp[-1])