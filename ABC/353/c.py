from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

a.sort()
s = [0]
for i in range(n):
    s.append(s[-1] + a[i])

ans = 0
limit = 10 ** 8
for i in range(n - 1):
    left = limit - a[i]
    idx = bisect_left(a, left)
    if idx == n:
        ans += a[i] * (n - i - 1) + s[-1] - s[i + 1]
    elif idx > i:
        ans += a[i] * (idx - i - 1) + s[idx] - s[i + 1]
        ans += a[i] * (n - idx) + s[-1] - s[idx] - limit * (n - idx)
    else:
        ans += a[i] * (n - i - 1) + s[-1] - s[i + 1] - limit * (n - i - 1)

print(ans)