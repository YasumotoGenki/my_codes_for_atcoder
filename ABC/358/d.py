n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
idx_a = 0
idx_b = 0
ans = []
while(idx_a < n and len(ans) < m):
    if b[idx_b] > a[idx_a]:
        idx_a += 1
    else:
        ans.append(a[idx_a])
        idx_a += 1
        idx_b += 1
if len(ans) < m:
    print(-1)
else:
    print(sum(ans))