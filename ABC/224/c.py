from itertools import combinations

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

ans = 0
for a, b, c in combinations(points, 3):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x1 -= x3
    x2 -= x3
    y1 -= y3
    y2 -= y3
    if x1 * y2 == x2 * y1:
        continue
    else:
        ans += 1

print(ans)



# for a, b, c in combinations(points, 3):
#     if (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2 == (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2:
#         continue
#     if (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 == (c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2:
#         continue
#     if (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2 + (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 == (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2:
#         continue
#     ans += 1