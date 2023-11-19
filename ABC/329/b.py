n = int(input())
a = list(map(int, input().split()))

max_value = max(a)
ans = 0
for item_a in a:
    if item_a != max_value:
        ans = max(ans, item_a)
print(ans)