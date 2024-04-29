n, m = map(int, input().split())

class UnionFind():
    def __init__(self, n):
        self.n = n
        # parents[i]: 要素iの親要素の番号
        # 要素iが根の場合、parents[i] = -(そのグループの要素数)
        self.parents = [-1] * n
        self.parents_node_num = [0] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.parents_node_num[x] += 1
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents_node_num[x] += self.parents_node_num[y] + 1
        self.parents[y] = x
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]

uf = UnionFind(n)

for _ in  range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)

ans = 0

for i in range(n):
    if uf.parents[i] == -1:
        continue
    if uf.parents[i] < -1:
        num = -uf.parents[i]
        ans += (num * (num - 1) // 2) - uf.parents_node_num[i]

print(ans)