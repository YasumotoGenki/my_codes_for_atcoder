n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q - p + 1):
    val_1, val_2 = a[p + i - 1], a[r + i - 1]
    a[p + i - 1], a[r + i - 1] = val_2, val_1

print(*a)