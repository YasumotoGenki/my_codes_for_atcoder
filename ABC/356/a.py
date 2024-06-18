n, l, r = map(int, input().split())

a = [i for i in range(1, n + 1)]

for i in range(r - l + 1):
    a[l + i - 1] = r - i

print(*a)
