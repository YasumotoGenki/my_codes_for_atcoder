n = int(input())
p = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(n):
    add = p[i] - i
    for j in range(-1, 2, 1):
        idx = add + j
        idx %= n
        dp[idx] += 1
print(max(dp))
