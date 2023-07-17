n, m  = map(int, input().split())

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
    # 要素xが属するグループの要素数を返す
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    # 全ての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    # グループの数を返す
    def group_count(self):
        return len(self.roots())
    # 辞書{根の要素: [そのグループに含まれる要素のリスト], ...}を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    # print()での表示用
    # all_group_members()をprintする
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

uf = UnionFind(n)
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.union(u, v)
k = int(input())
all_false_flg = False
parent_set = set()
for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if uf.same(x, y):
        all_false_flg = True
    else:
        parent_x = uf.find(x)
        parent_y = uf.find(y)
        parent_set.add(tuple([parent_x, parent_y]))
        parent_set.add(tuple([parent_y, parent_x]))

Q = int(input())
for i in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    parent_p = uf.find(p)
    parent_q = uf.find(q)
    if all_false_flg or tuple([parent_p, parent_q]) in parent_set:
        print("No")
    else:
        print("Yes")