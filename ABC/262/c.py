n = int(input())
a = list(map(int, input().split()))

count = 0
s = set()
for i in range(n):
    if a[i] == i + 1:
        count += 1
        s.add(i)

ans = 0
if count >= 2:
    ans += count * (count - 1) // 2

tmp = 0
for i in range(n):
    if i not in s and a[a[i] - 1] == i + 1:
        tmp += 1
ans += tmp // 2

print(ans)