n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
cur = 0
idx = 0
while(idx < n):
    if cur + a[idx] <= k:
        cur += a[idx]
        idx += 1
    else:
        ans += 1
        cur = 0

ans += 1
print(ans)