n, m, k = map(int, input().split())
mod = 998244353

a = [[0 for i in range(m)] for j in range(n)]
a[0] = [1 for i in range(m)]


for i in range(n - 1):
    stack = sum(a[i][k:])
    for j in range(m):
        a[i + 1][j] += stack
        a[i + 1][j] %= mod
        if j - k + 1 >= 0 and j - k + 1 < m:
            stack += a[i][j - k + 1]
        if j + k < m:
            stack -= a[i][j + k]
print(sum(a[-1]) % mod)