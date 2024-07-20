from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append([v, b])
    edges[v].append([u, b])

INF = 10 ** 20
weight = [INF for _ in range(n)]
que = deque([[a[0], 0]])
weight[0] = a[0]

while(que):
    cur_weight, cur_node = que.popleft()
    if cur_weight != weight[cur_node]:
        continue
    for next_node, b in edges[cur_node]:
        if weight[next_node] > weight[cur_node] + b + a[next_node]:
            weight[next_node] = weight[cur_node] + b + a[next_node]
            que.append([weight[next_node], next_node])

print(*weight[1:])
            