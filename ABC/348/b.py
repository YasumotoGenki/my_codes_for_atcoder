n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

for i, (x, y) in enumerate(xy):
    max_value = 0
    max_idx = 0
    for j, (xx, yy) in enumerate(xy):
        if i == j:
            continue
        if max_value < (x - xx) ** 2 + (y - yy) ** 2:
            max_value = (x - xx) ** 2 + (y - yy) ** 2
            max_idx = j + 1
    print(max_idx)
