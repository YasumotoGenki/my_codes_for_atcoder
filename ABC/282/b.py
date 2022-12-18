n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        flg = True
        for k in range(m):
            if s[i][k] == "x" and s[j][k] == "x":
                flg = False
                break
        if flg:
            ans += 1
print(ans)