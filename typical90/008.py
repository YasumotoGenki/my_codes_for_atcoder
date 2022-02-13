n = int(input())
s = input()
mod = 10 ** 9 + 7

ans = [0] * (len('atcoder') + 1)
ans[0] = 1

for i in range(n):
    for j, c in enumerate('atcoder'):
        if s[i] == c:
            ans[j + 1] += ans[j]
            ans[j + 1] %= mod
print(ans[-1])