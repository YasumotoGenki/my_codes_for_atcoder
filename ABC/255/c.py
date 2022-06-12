from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = [0]
stack = 0
for i in range(n):
    stack += a[i]
    s.append(stack)

for i in range(q):
    x = int(input())
    idx = bisect_left(a, x)
    low = s[idx]
    high = s[-1] - s[idx]
    ans = x * idx - low + high - x * (n - idx)
    print(ans)