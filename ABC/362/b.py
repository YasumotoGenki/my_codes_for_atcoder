xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())


def calc_powered_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

dist_1 = calc_powered_dist(xa, ya, xb, yb)
dist_2 = calc_powered_dist(xb, yb, xc, yc)
dist_3 = calc_powered_dist(xc, yc, xa, ya)

ans = False
if dist_1 + dist_2 == dist_3:
    ans = True
elif dist_2 + dist_3 == dist_1:
    ans = True
elif dist_3 + dist_1 == dist_2:
    ans = True

if ans:
    print("Yes")
else:
    print("No")