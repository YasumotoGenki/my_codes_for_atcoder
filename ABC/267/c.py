n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0]
for item_a in a:
    s.append(s[-1] + item_a)

cur = 0
ans = 0
for i in range(n - m + 1):
    if i == 0:
        for j in range(m):
            cur += (a[j] * (j + 1))
        ans = cur
    else:
        cur -= (s[i + m - 1] - s[i - 1])
        cur += (a[i + m - 1] * m)
        ans = max(ans, cur)
print(ans)