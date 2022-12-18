n, m = map(int, input().split())
edges = dict()
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u in edges:
        edges[u].add(v)
    else:
        edges[u] = {v}
    if v in edges:
        edges[v].add(u)
    else:
        edges[v] = {u}

# 2部グラフなので、01でどちらに属するのかを表現、Noneの場合はどちらでもない
nodes = [None] * n

que = []
idx = 0

for i in range(n):
    if i in edges:
        que.append(i)
        idx = i
        break

zero_count = 0
one_count = 0
ans = n * (n - 1) // 2 - m

while(que):
    cur_node = que.pop()
    if nodes[cur_node] is None:
        nodes[cur_node] = 0
        zero_count += 1
    if cur_node in edges:
        for next_node in edges[cur_node]:
            if nodes[next_node] is None:
                if nodes[cur_node] == 1:
                    nodes[next_node] = 0
                    zero_count += 1
                else:
                    nodes[next_node] = 1
                    one_count += 1
                que.append(next_node)
            elif nodes[cur_node] == nodes[next_node]:
                print(0)
                exit()
            else:
                pass
    if len(que) == 0:
        ans -= zero_count * (zero_count - 1) // 2
        ans -= one_count * (one_count - 1) // 2
        while(idx < n - 1 and not que):
            idx += 1
            if nodes[idx] is None:
                que.append(idx)
        zero_count = 0
        one_count = 0

print(ans)