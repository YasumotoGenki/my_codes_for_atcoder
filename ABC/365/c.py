n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) <= m:
    print("infinite")
    exit()

ok = 0
ng = m + 1

while(ng - ok > 1):
    middle = (ok + ng) //  2
    total = 0
    for i in range(n):
        total += min(middle, a[i])
    if total > m:
        ng = middle
    else:
        ok = middle

print(ok)