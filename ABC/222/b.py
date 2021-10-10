n, p = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for a_item in a:
    if a_item < p:
        ans += 1
print(ans)