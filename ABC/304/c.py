n, d = map(int, input().split())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    xy.append([x, y])

# define Union Find
class UnionFind():
    def __init__(self, n):
        self.n = n
        # parents[i]: 要素iの親要素の番号
        # 要素iが根の場合、parents[i] = -(そのグループの要素数)
        self.parents = [-1] * n
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
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

uf = UnionFind(n)

for i in range(n):
    for j in range(i + 1, n):
        # Judge whether 2 point is in D or not
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if d ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:
            uf.union(i, j)

infected_list = uf.members(0)
ans = [False for _ in range(n)]
for idx in infected_list:
    ans[idx] = True

for i in range(n):
    if ans[i]:
        print("Yes")
    else:
        print("No")