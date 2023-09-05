n, m, p = map(int, input().split())

if n < m:
    print(0)
    exit()

ans = 1
ans += (n - m) // p
print(ans)