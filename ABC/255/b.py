from decimal import MAX_EMAX
from math import sqrt

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = []
for i in range(n):
    x, y = list(map(int, input().split()))
    xy.append([x, y])

ans = 0
for i in range(n):
    max_distance = 1000000000
    for item_a in a:
        item_a -= 1
        x1, y1 = xy[i]
        x2, y2 = xy[item_a]
        distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        max_distance = min(distance, max_distance)
    ans = max(ans, max_distance)

print(ans)
