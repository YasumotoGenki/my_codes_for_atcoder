n, d = map(int, input().split())
snakes = []
for i in range(n):
    t, l = map(int, input().split())
    snakes.append([t, l])

for k in range(1, d + 1):
    ans = 0
    for i in range(n):
        t, l = snakes[i]
        ans = max(ans, t * (l + k))
    print(ans)
