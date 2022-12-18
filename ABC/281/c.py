from bisect import bisect_left


n, t = map(int, input().split())
a = list(map(int, input().split()))

s = [0]
for i in range(n):
    s.append(s[-1] + a[i])

t %= s[-1]
idx = bisect_left(s, t)
if idx == 0:
    print(n, 0)
else:
    print(idx, t - s[idx - 1])