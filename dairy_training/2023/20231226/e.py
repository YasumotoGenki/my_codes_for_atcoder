n = int(input())
a = list(map(int, input().split()))
ans = 0
stack = set()
for i in range(n):
    if a[i] not in stack:
        stack.add(a[i])
    else:
        ans += 1
        stack.remove(a[i])
print(ans)