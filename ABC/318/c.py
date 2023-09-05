from bisect import bisect_right

n, d, p = map(int, input().split())
f = list(map(int, input().split()))

cost_tour_ticket = p / d

f.sort(reverse=True)
ans = 0
for idx in range(0, n, d):
    if sum(f[idx: idx + d]) > p:
        ans +=  p
    else:
        ans += sum(f[idx: idx + d])

print(ans)