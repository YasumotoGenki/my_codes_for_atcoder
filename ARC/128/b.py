t = int(input())

for i in range(t):
    ans = 10 ** 10
    r, g, b = map(int, input().split())
    if (r % 3 == g % 3):
        ans = min(ans, max(r, g))
    if (g % 3 == b % 3):
        ans = min(ans, max(g, b))
    if (b % 3 == r % 3):
        ans = min(ans, max(b, r))
    if ans != 10 ** 10:
        print(ans)
    else:
        print(-1)