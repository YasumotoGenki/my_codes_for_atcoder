n = int(input())
a = list(map(int, input().split()))

ans = []
ans.append(a[0])

for i in range(n - 1):
    if abs(a[i] - a[i + 1]) == 1:
        pass
    elif a[i] > a[i + 1] + 1:
        for item in range(a[i] - 1, a[i + 1], -1):
            ans.append(item)
    elif a[i] + 1 < a[i + 1]:
        for item in range(a[i] + 1, a[i + 1], 1):
            ans.append(item)
    ans.append(a[i + 1])
print(*ans)
