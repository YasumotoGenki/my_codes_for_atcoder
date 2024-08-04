n = int(input())
a = list(map(int, input().split()))

bit = [[0 for _ in range(20)] for _ in range(n + 1)]
rev_bit = [[0 for _ in range(20)] for _ in range(n + 1)]
s = [[0 for _ in range(20)] for _ in range(n + 1)]
s0 = [[0 for _ in range(20)] for _ in range(n + 1)]
s1 = [[0 for _ in range(20)] for _ in range(n + 1)]
# bitごとの累積和を求める
# ただし、累積和はxorで0or1で表現する
for i in range(n):
    for j in range(20):
        b = 0
        if a[i] & 1 << j:
            b = 1
        rev_bit[i + 1][j] = rev_bit[i][j] ^ b
        bit[i + 1][j] = b

for i in range(n):
    for j in range(20):
        s[i + 1][j] = s[i][j] + (1 if rev_bit[i][j] else 0)
        if bit[i + 1][j] == 1:
            s1[i + 1][j] = s1[i][j] + 1
            s0[i + 1][j] = s0[i][j]
        else:
            s1[i + 1][j] = s1[i][j]
            s0[i + 1][j] = s0[i][j] + 1

ans = 0
# 前から順に累積和を利用して、ビット数だけansに加算する
for i in range(n - 1):
    for j in range(20):
        ans += (s[-1][j] - s[i + 1][j]) * (1 << j)
        # if dp[i + 1][j] == 0:
        #     ans += (s1[-1][j] - s1[i + 1][j]) * (1 << j)
        # else:
        #     ans += (s0[-1][j] - s0[i + 1][j]) * (1 << j)

print(ans)