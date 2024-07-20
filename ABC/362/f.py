import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())

tree = [[] for _ in range(n)]

for _ in range(n  - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    tree[u].append(v)
    tree[v].append(u)

dfs_arr = []

def dfs(node, parent):
    for neighbor in tree[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node)
    dfs_arr.append(node)
        
# 各ノードの部分木のサイズを保持するリスト
subtree_size = [0] * n
def dfs_size(node, parent):    
    subtree_size[node] = 1
    for neighbor in tree[node]:
        if neighbor == parent:
            continue
        subtree_size[node] += dfs_size(neighbor, node)
        
    return subtree_size[node]

# DFSを使用して部分木のサイズを計算
dfs_size(0, -1)

def find_centroid(node, parent):    
    # DFSを使用して重心を見つける
    for neighbor in tree[node]:
        if neighbor == parent:
            continue
        if subtree_size[neighbor] > n // 2:
            return find_centroid(neighbor, node)
    return node
    
# 重心を見つける
centroid = find_centroid(0, -1)
dfs(centroid, -1)

for i in range(n // 2):
    print(dfs_arr[i] + 1, dfs_arr[i + n // 2] + 1)