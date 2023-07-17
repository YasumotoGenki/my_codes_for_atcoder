n = int(input())
uv = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv[u].append(v)
    uv[v].append(u)

ans = []
count_remained_nodes = n
for i in range(n):
    if len(uv[i]) > 2:
        ans.append(len(uv[i]))
        count_remained_nodes -= (len(uv[i]) + 1)

while(count_remained_nodes > 0):
    count_remained_nodes -= 3
    ans.append(2)

ans.sort()
print(*ans)