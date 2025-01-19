from  bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 1, -1, -1):
    length = a[i] // 2
    idx = bisect_right(a, length)
    ans += idx

print(ans)
