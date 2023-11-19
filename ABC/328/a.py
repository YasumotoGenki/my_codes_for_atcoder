n, x = map(int, input().split())
s = list(map(int, input().split()))

s.sort()
ans = 0
for i in range(n):
    if s[i] > x:
        break
    else:
        ans += s[i]
print(ans)