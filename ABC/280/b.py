n = int(input())
s = list(map(int, input().split()))

ans = []
cur_sum = 0

for i in range(n):
    if i == 0:
        ans.append(s[i])
    else:
        ans.append(s[i] - cur_sum)
    cur_sum += ans[-1]
print(*ans)