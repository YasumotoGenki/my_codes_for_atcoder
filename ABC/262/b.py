n, m = map(int, input().split())
nodes = [set() for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].add(v)
    nodes[v].add(u)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if i in nodes[j] and j in nodes[k] and k in nodes[i]:
                ans += 1
print(ans)
