from math import ceil

n, l, w = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
edge = 0
for i in range(n):
    if edge < a[i]:
        ans += (a[i] - edge) // w
        if (a[i] - edge) % w:
            ans += 1
    edge = a[i] + w
else:
    if edge < l:
        ans += (l - edge) // w
        if (l - edge) % w:
            ans += 1

print(ans)