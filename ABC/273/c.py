from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(list(set(a)))
kinds = len(sorted_a)
ans = [0] * n
for i in range(n):
    idx = bisect_right(sorted_a, a[i])
    ans[kinds - idx] += 1

for item in ans:
    print(item)