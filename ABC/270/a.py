a, b = map(int, input().split())
ans = 0
for i in range(3):
    cur = 1 << i
    if a & cur or b & cur:
        ans += cur
print(ans)