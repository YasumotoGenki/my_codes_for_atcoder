n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

if t in set(c):
    color = t
else:
    color = c[0]

max_value = -1
ans = -1
for i in range(n):
    if c[i] == color:
        if max_value < r[i]:
            max_value = r[i]
            ans = i + 1

print(ans)