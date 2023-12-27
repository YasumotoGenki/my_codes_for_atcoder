from bisect import bisect_right

n, q = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
s = [0]
for i in range(n):
    s.append(s[-1] + r[i])
for i in range(q):
    tonakai_num = int(input())
    ans = bisect_right(s, tonakai_num) - 1
    print(ans)
