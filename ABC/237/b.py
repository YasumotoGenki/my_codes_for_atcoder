h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))

ans = [[None] * h for i in range(w)]
for i in range(w):
    for j in range(h):
        ans[i][j] = a[j][i]

for i in range(w):
    print(*ans[i])