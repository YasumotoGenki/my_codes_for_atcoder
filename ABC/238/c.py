n = int(input())
mod = 998244353

digit = len(str(n))
ans = 0

for i in range(digit):
    if i == digit - 1:
        a = 1 # initial term
        l = n - (10 ** i) + 1 # last term
        k = l - a + 1 # number of items
        ans += (a + l) * k // 2
        ans %= mod
    else:
        a = 1 # initial term
        l = 9 * (10 ** i) # last term
        k = 9 * (10 ** i) # number of items
        ans += (a + l) * k // 2
        ans %= mod
print(ans)