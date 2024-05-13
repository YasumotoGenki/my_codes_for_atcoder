import heapq

class UnionFind():
    def __init__(self, n):
        self.n = n
        # parents[i]: 要素iの親要素の番号
        # 要素iが根の場合、parents[i] = -(そのグループの要素数)
        self.parents = [-1] * n
        self.ans = 0
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
    def union_cost(self, x, y, c):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.ans += c
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]


n, m = map(int,input().split())
uf = UnionFind(n)
edge = []

for _ in range(m):
    k, c = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k - 1):
        small = a[i] - 1
        large = a[i + 1] - 1
        uf.union(small, large)
        heapq.heappush(edge, [c, small, large])

if uf.size(0) != n:
    print(-1)
    exit()

uf = UnionFind(n)
while(edge):
    c, small, large = heapq.heappop(edge)
    uf.union_cost(small, large, c)
print(uf.ans)