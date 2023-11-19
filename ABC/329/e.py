n, m = map(int, input().split())
s = input()
t = input()

dp = [[False for _ in range(m)] for _ in range(n)]
if s[-1] == t[-1]:
    dp[-1][-1] = True
else:
    print("No")
    exit()

for s_idx in range(n - 1, -1, -1):
    for t_idx in range(m):
        if dp[s_idx][t_idx]:
            if t_idx == 0:
                next_t_idx_candidates = list(range(m))
            else:
                next_t_idx_candidates = [t_idx - 1, m - 1]
            for next_t_idx in next_t_idx_candidates:
                if s[s_idx - 1] == t[next_t_idx]:
                    dp[s_idx - 1][next_t_idx] = True
if dp[0][0]:
    print("Yes")
else:
    print("No")
