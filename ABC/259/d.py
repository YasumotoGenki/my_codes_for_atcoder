import math

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
    def same(self, x, y):
        return self.find(x) == self.find(y)

############################################################
############################################################

n = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = []
for i in range(n):
    xyr.append(list(map(int, input().split())))

s_circle_list, t_circle_list = [], []

for i in range(n):
    x, y, r = xyr[i]
    if (x - sx) ** 2 + (y - sy) ** 2 == r ** 2:
        s_circle_list.append(i)
    if (x - tx) ** 2 + (y - ty) ** 2 == r ** 2:
        t_circle_list.append(i)

uf = UnionFind(n)

for i in range(n):
    for j in range(i + 1, n):
        ix, iy, ir = xyr[i]
        jx, jy, jr = xyr[j]
        if (ir - jr) ** 2 <= (ix - jx) ** 2 + (iy - jy) ** 2 <= (ir + jr) ** 2:
            uf.union(i, j)
for s_idx in s_circle_list:
    for t_idx in t_circle_list:
        if uf.same(s_idx, t_idx):
            print("Yes")
            exit()
print("No")

# ref: https://www.try-it.jp/chapters-6533/sections-6587/lessons-6636/example-2/#:~:text=2%E3%81%A4%E3%81%AE%E5%86%86%E3%81%8C2%E7%82%B9%E3%81%A7%E4%BA%A4%E3%82%8F%E3%82%8B%E6%9D%A1%E4%BB%B6%E3%81%AF,%E5%B0%8F%E3%81%95%E3%81%84%E3%81%A8%E3%81%8D%20%E3%81%A7%E3%81%97%E3%81%9F%E3%81%AD%EF%BC%81