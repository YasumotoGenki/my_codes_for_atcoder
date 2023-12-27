n = int(input())
edges = [set() for _ in range(n)]

for i in range(n - 1):
    v, u = map(int, input().split())
    v -= 1
    u -= 1
    edges[v].add(u)
    edges[u].add(v)

if len(edges[0]) == 1:
    print(1)
    exit()

count_list = []
for next_node in edges[0]:
    count = 0
    que = []
    visited_set = set([0, next_node])
    que.append(next_node)
    while(que):
        popped_node = que.pop()
        for node in edges[popped_node]:
            if node in visited_set:
                continue
            que.append(node)
            visited_set.add(node)
        count += 1
    count_list.append(count)
count_list.sort()
print(sum(count_list) - count_list[-1] + 1)