n, m = map(int, input().split())
not_friendly_list = [[i for i in range(n) if i != j] for j in range(n)]
for i in range(m):
    a = list(map(int, input().split()))
    for j in range(n - 1):
        left = a[j] - 1
        right= a[j + 1] - 1
        if right in not_friendly_list[left]:
            idx = not_friendly_list[left].index(right)
            not_friendly_list[left].pop(idx)
        if left in not_friendly_list[right]:
            idx = not_friendly_list[right].index(left)
            not_friendly_list[right].pop(idx)

ans = 0
for i in range(n):
    ans += len(not_friendly_list[i])
ans //= 2
print(ans)
