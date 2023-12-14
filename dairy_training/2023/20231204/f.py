n, m = map(int, input().split())
route = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    route[a][b] = max(route[a][b], c)
    route[b][a] = max(route[b][a], c)

ans = -1
all_nodes_set = set([i for i in range(n)])
def bfs(visited_nodes_set, not_visited_set, current_node, costs):
    global route
    global ans
    global all_nodes_set
    ans = max(ans, costs)
    for next_node in not_visited_set:
        if route[current_node][next_node] > 0:
            bfs(visited_nodes_set | set([next_node]), not_visited_set - set([next_node]), next_node, costs + route[current_node][next_node])

for i in range(n):
    bfs(set([i]), all_nodes_set - set([i]), i, 0)

print(ans)