n, m = map(int, input().split())
ab = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a in ab:
        ab[a] += [b]
    else:
        ab[a] = [b]
    if b in ab:
        ab[b] += [a]
    else:
        ab[b] = [a]

for i in range(1, n + 1):
    if i not in ab:
        count = 0
        print(count)
    else:
        count = len(ab[i])
        ab[i].sort()
        print(count, *ab[i])