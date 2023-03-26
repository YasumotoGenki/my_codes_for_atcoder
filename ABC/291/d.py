mod = 998244353
n = int(input())
list_a, list_b = [], []
for i in range(n):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

dp = [[0, 0] for _ in range(n)]
dp[0] =  [1, 1]
for i in range(1, n):
    for cur_ab_idx in ['a', 'b']:
        for pre_ab_idx in ['a', 'b']:
            if cur_ab_idx == 'a' and pre_ab_idx == 'a':
                if list_a[i - 1] != list_a[i]:
                    dp[i][0] += dp[i - 1][0]
                    dp[i][0] %= mod
            elif cur_ab_idx == 'a' and pre_ab_idx == 'b':
                if list_b[i - 1] != list_a[i]:
                    dp[i][0] += dp[i - 1][1]
                    dp[i][0] %= mod
            elif cur_ab_idx == 'b' and pre_ab_idx == 'a':
                if list_a[i - 1] != list_b[i]:
                    dp[i][1] += dp[i - 1][0]
                    dp[i][1] %= mod
            elif cur_ab_idx == 'b' and pre_ab_idx == 'b':
                if list_b[i - 1] != list_b[i]:
                    dp[i][1] += dp[i - 1][1]
                    dp[i][1] %= mod
ans = sum(dp[-1])
ans %= mod
print(ans)