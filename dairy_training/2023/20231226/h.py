from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
a = list(map(int, input().split()))
uv = [[] for  _ in range(n)]
cost = [0 for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uv[u].append(v)
    uv[v].append(u)
    cost[u] += a[v]
    cost[v] += a[u]

def judge(value):
    used = set()
    que = deque()
    current_cost = deepcopy(cost)
    for i in range(n):
        if current_cost[i] <= value:
            que.append(i)
            used.add(i)
    while(que):
        node = que.pop()
        for next_node in uv[node]:
            current_cost[next_node] -= a[node]
            if next_node not in used and current_cost[next_node] <= value:
                que.append(next_node)
                used.add(next_node)
    if len(used) == n:
        return True
    else:
        return False


left, right = -1,  10 ** 16

while(right - left > 1):
    middle = (right + left) // 2
    if judge(middle):
        right = middle
    else:
        left = middle
print(right)