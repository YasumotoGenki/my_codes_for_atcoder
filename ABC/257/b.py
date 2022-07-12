n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for item_l in l:
    cur = a[item_l - 1]
    if item_l == k:
        if a[item_l - 1] != n:
            a[item_l - 1] += 1
    else:
        if cur < a[item_l] - 1:
            a[item_l - 1] += 1
print(*a)