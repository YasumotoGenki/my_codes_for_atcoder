from itertools import permutations

n, m = map(int, input().split())
edge = [[[] for _ in range(n)] for _ in range(n)]
bridges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    edge[u][v].append(t)
    edge[v][u].append(t)
    bridges.append([u, v, t])

INF = 10 ** 50
cost_list = [[INF for _ in range(n)] for _ in range(n)]

# sort
for i in range(n):
    for j in range(n):
        if i == j:
            cost_list[i][j] = 0
        if edge[i][j]:
            edge[i][j].sort()
            cost_list[i][j] = edge[i][j][0]

# floyd_warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost_list[i][j] = min(cost_list[i][j], cost_list[i][k] + cost_list[k][j])

# read queries
q = int(input())
for q_idx in range(q):
    k = int(input())
    b = list(map(int, input().split()))
    b = [item - 1 for item in b]
    ans = INF
    for bridge_indices in permutations(range(k)):
        cur = 0
        cur_node_cost = [[0, 0]]
        next_node_cost = [[0, INF], [0, INF]]
        for idx in bridge_indices:
            bridge_idx = b[idx]
            u, v, t = bridges[bridge_idx]
            for cur_node, cost in cur_node_cost:
                next_node_cost[0] = [u, min(cost + cost_list[cur_node][v] + t, next_node_cost[0][1])]
                next_node_cost[1] = [v, min(cost + cost_list[cur_node][u] + t, next_node_cost[1][1])]
            cur_node_cost = next_node_cost
            next_node_cost = [[0, INF], [0, INF]]
        for cur_node, cost in cur_node_cost:
            ans = min(ans, cost + cost_list[cur_node][n - 1])
    print(ans)