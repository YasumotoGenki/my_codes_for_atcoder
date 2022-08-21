n, m, t = map(int, input().split())
a = list(map(int, input().split()))
xy =[0 for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    xy[x] = y

for i in range(n - 1):
    t -= a[i]
    if t <= 0:
        print("No")
        exit()
    if xy[i + 1] > 0:
        t += xy[i + 1]
print("Yes")