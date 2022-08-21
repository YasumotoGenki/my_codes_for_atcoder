n = int(input())
p = list(map(int, input().split()))

idx = -1
ans = 0
while(True):
    idx = p[idx]
    if idx == 1:
        ans += 1
        break
    idx -= 2
    ans += 1
print(ans)