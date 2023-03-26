n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i, item in enumerate(sorted(list(set(a)))):
    if i == k:
        break
    if item == i:
        ans += 1
    else:
        break
print(ans)