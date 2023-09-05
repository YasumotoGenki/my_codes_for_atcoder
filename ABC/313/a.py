n = int(input())
p = list(map(int,  input().split()))

ans = 0
for i in range(1, n):
    if p[0] + ans <= p[i]:
        ans = p[i] - p[0] + 1
print(ans)