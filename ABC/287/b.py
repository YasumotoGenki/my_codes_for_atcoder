n, m = map(int, input().split())
s, t = [], []
for i in range(n):
    s.append(input())
for i in range(m):
    t.append(input())

ans = 0
for i in range(n):
    if s[i][-3:] in t:
        ans += 1
print(ans)