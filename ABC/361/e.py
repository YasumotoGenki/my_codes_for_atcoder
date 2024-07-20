import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

n = int(input())
edges = [[] for _ in range(n)]
total = 0
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append([b, c])
    edges[b].append([a, c])
    total += c

def bfs(start_node):
    max_dist = 0
    max_node = start_node
    dist = [-1] * n
    dist[start_node] = 0
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        for next_node, cost in edges[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + cost
                queue.append(next_node)
                if dist[next_node] > max_dist:
                    max_dist = dist[next_node]
                    max_node = next_node
    return max_node, max_dist

# 一度目のBFSで最も遠いノードを見つける
farthest_node, _ = bfs(0)
# 二度目のBFSで木の直径を求める
_, max_distance = bfs(farthest_node)

print(2 * total - max_distance)
