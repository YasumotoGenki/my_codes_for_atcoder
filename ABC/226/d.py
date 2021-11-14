from itertools import combinations
import math

n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
idx_list = [i for i in range(n)]
ans_set = set()
for p1_idx, p2_idx in combinations(idx_list, 2):
    x1, y1 = xy[p1_idx]
    x2, y2 = xy[p2_idx]
    diff_x = x2 - x1
    diff_y = y2 - y1
    r = math.gcd(abs(diff_x), abs(diff_y))
    diff_x //= r
    diff_y //= r
    if diff_x == 0:
        diff_y = 1
    elif diff_y == 0:
        diffx = 1
    if diff_x < 0:
        diff_x *= -1
        diff_y *= -1
    ans_set.add(tuple([diff_x, diff_y]))
print(len(ans_set) * 2)