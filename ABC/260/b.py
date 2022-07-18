n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ai, bi, si = [], [], []
for i in range(n):
    ai.append([a[i], -i])
    bi.append([b[i], -i])
    si.append([a[i] + b[i], -i])

ai.sort(key=lambda x: (x[0], x[1]), reverse=True)
bi.sort(key=lambda x: (x[0], x[1]), reverse=True)
si.sort(key=lambda x: (x[0], x[1]), reverse=True)

ans = set()
for i in range(x):
    item, idx = ai[i]
    ans.add(-idx + 1)

i = 0
j = 0
while(j < y and i < n):
    item, idx = bi[i]
    if -idx + 1 not in ans:
        ans.add(-idx + 1)
        j += 1
    i += 1

i = 0
j = 0
while(j < z and i < n):
    item, idx = si[i]
    if -idx + 1 not in ans:
        ans.add(-idx + 1)
        j += 1
    i += 1

ans = list(ans)
ans.sort()
for item in ans:
    print(item)