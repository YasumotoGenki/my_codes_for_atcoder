mod = 998244353

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())


# area 1: point (x1, y1)
# area 2: points (x, y) where x != x1 and y != y1
# area 3: points (x1, y) where y = y1 and x != x1
# area 4: points (x, y1) where x = x1 and y != y1

area_1 = 0
area_2 = 0
area_3 = 0
area_4 = 0

for i in range(K):
    if i == 0:
        area_1 = 0
        area_2 = 0
        area_3 = 1
        area_4 = 1
    else:
        new_area_1 = (W - 1) * area_3 + (H - 1) * area_4
        new_area_1 %= mod
        new_area_2 = (W + H - 4) * area_2 + area_3 + area_4
        new_area_2 %= mod
        new_area_3 = (W - 2) * area_3 + area_1 + (H - 1) * area_2
        new_area_3 %= mod
        new_area_4 = (H - 2) * area_4 + area_1 + (W - 1) * area_2
        new_area_4 %= mod
        area_1, area_2, area_3, area_4 = new_area_1, new_area_2, new_area_3, new_area_4

if x1 == x2 and y1 == y2:
    print(area_1)
elif x1 != x2 and y1 != y2:
    print(area_2)
elif x1 == x2:
    print(area_3)
elif y1 == y2:
    print(area_4)