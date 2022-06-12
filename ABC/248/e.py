from itertools import combinations

n, k = map(int, input().split())
if k == 1:
    print("Infinity")
    exit()

xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

ans = 0
ans_s = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (i, j) in ans_s or (j, i) in ans_s:
            continue
        count = 0
        s = set()
        s.add(i)
        s.add(j)
        for l in range(n):
            # check 3 points are on the same line
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[l]
            if (y3 - y1) * (x2 - x1) == (x3 - x1) * (y2 - y1):
                count += 1
                s.add(l)
        if count >= k:
            ans += 1
            for w, v in combinations(s, 2):
                ans_s.add((w, v))
print(ans)