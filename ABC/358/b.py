n, a = map(int, input().split())
t = list(map(int, input().split()))

cur = 0
for i in range(n):
    if cur < t[i]:
        cur = t[i] + a
    else:
        cur += a
    print(cur)
