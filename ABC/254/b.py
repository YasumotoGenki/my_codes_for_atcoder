n = int(input())
ans = []
for i in range(n):
    if i == 0:
        ans = [1]
        print(*ans)
    else:
        cur = []
        for j in range(i + 1):
            if j == 0 or i == j:
                cur.append(1)
            else:
                cur.append(ans[i - 1][j - 1] + ans[i - 1][j])
        ans.append(cur)
        print(*ans[-1])