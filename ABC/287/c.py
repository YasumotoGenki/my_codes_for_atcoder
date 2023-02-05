n, m = map(int, input().split())

if m != n - 1:
    print("No")
    exit()

uv = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv[u].append(v)
    uv[v].append(u)

count = 0
initial_nodes = []
for i in range(n):
    if len(uv[i]) == 1:
        count += 1
        initial_nodes.append(i)
    elif len(uv[i]) == 2:
        pass
    else:
        print("No")
        exit()
if count != 2:
    print("No")
    exit()

que = [initial_nodes[0]]
done = set()

while(que):
    cur_node = que.pop()
    done.add(cur_node)
    if len(done) == n and cur_node == initial_nodes[-1]:
        print("Yes")
        exit()
    
    for next_node in uv[cur_node]:
        if next_node not in done:
            que.append(next_node)
print("No")