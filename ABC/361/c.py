n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 10 ** 20

for i in range(k + 1):
    ans = min(ans, a[i + n - k - 1] - a[i])

print(ans)