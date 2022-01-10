from itertools import combinations
import math

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

ans = 0

for p1, p2 in combinations(xy, 2):
    x1, y1 = p1
    x2, y2 = p2
    ans = max(ans, math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
print(ans)