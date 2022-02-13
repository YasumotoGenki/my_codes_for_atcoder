from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
q = int(input())
a.sort()
for i in range(q):
    ans = 0
    b = int(input())
    k = bisect_left(a, b)
    if 0 < k and k < n:
        ans += min(abs(a[k] - b), abs(a[k - 1] - b))
    elif k == 0:
        ans += abs(a[k] - b)
    elif k > n - 1:
        ans += abs(a[n - 1] - b)
    print(ans)