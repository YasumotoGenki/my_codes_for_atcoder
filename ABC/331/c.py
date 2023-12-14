from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))

s = [0]
sorted_a = sorted(a)

for item in sorted_a:
    s.append(s[-1] + item)

ans = []
for i in range(n):
    current_num = a[i]
    idx = bisect_right(sorted_a, current_num)
    if idx >= n:
        ans.append(0)
    else:
        ans.append(s[-1] - s[idx])
print(*ans)