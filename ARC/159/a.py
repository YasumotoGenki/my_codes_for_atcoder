n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

cost_table = [[1000 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            cost_table[i][j] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if cost_table[j][i] != 1000 and cost_table[i][k] != 1000:
                cost_table[j][k] = min(cost_table[j][k], cost_table[j][i] + cost_table[i][k])

q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    s = s % n - 1
    t = t % n - 1
    ans = cost_table[s][t]
    if ans == 1000:
        ans = -1
    print(ans)



# node_2_node_list = []

# for i in range(n):
#     can_go = [[-1 for _ in range(n)] for _ in range(n)]
#     queue = []
#     for j in range(n):
#         if a[i][j] == 1:
#             queue.append(j)
#             can_go[i][j] = 1
#     while(queue):
#         next_node = queue.pop()
#         cost = can_go[i][next_node]
#         if can_go[i][next_node] == -1:
#             can_go[i][next_node] = cost + 1
#             queue.append(next_node)
#         elif can_go[i][next_node] > cost + 1:
#             can_go[i][next_node] = cost + 1
#             queue.append(next_node)
#     node_2_node_list.append(can_go[i])

