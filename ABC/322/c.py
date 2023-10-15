n, m = map(int, input().split())
a = list(map(int, input().split()))

a_idx = 0
for i in range(1, n + 1):
    if a[a_idx] == i:
        print(0)
        a_idx += 1
    else:
        print(a[a_idx] - i)