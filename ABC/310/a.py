n, p, q = map(int, input().split())
d = list(map(int, input().split()))

ans = p
for i in range(n):
    if d[i] + q < ans:
        ans = d[i] + q

print(ans)