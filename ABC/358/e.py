k = int(input())
c = list(map(int, input().split()))

list_nCr = [[1] for _ in range(k + 1)]
list_pow26 = [1, 26]
mod = 998244353

n1 = [1] * (k + 1)
for i in range(2, k + 1):
    n1[i] = (n1[i - 1] * i) % mod
n2 = [1] * (k + 1)
for i in range(2, k + 1):
    n2[i] = pow(n1[i], mod - 2, mod)


def comb(N, R, mod=mod):
    return (n1[N] * (n2[N - R] * n2[R]) % mod) % mod

ans = 0
dp = [0] * (k + 1)
dp[0] = 1

for i in range(26):
    prev_dp = dp[:]
    for j in range(k + 1):
        for a in range(1, c[i] + 1):
            nj = j + a
            if nj > k:
                break
            dp[nj] += prev_dp[j] * comb(nj, a)

print((sum(dp) - 1) % mod)