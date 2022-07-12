n, m, x, t, d = map(int, input().split())

if m <= x:
    ans = t - (x - m) * d
else:
    ans = t

print(ans)