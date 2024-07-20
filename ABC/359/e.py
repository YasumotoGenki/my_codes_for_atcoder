n = int(input())
h = list(map(int, input().split()))
sorted_h = sorted(h)

# 座標圧縮
coordinate2idx = dict()
for i in range(n):
    coordinate2idx[sorted_h[i]] = i

# segment tree
class SegmentTree:
    def __init__(self, op, e, n, v=None):
        self.op = op
        self.e = e
        self.n = n
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [e] * (2 * self.size)

        if v is not None:
            for i in range(n):
                self.data[self.size + i] = v[i]
            for i in range(self.size - 1, 0, -1):
                self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])

    def update(self, idx, value):
        idx += self.size
        self.data[idx] = value
        while idx > 1:
            idx //= 2
            self.data[idx] = self.op(self.data[2 * idx], self.data[2 * idx + 1])

    def query(self, l, r):
        res = self.e
        l += self.size
        r += self.size
        while l < r:
            if l % 2 == 1:
                res = self.op(res, self.data[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.op(res, self.data[r])
            l //= 2
            r //= 2
        return res

op = max
e = 0
segment_tree = SegmentTree(op, e, n=n+1)

s = 0
ans = [0]
max_wall = 0

for i in range(n):
    # s += h[i] + 1
    prev_idx = segment_tree.query(coordinate2idx[h[i]] + 1, n + 1)
    # if h[i] * (i - prev_idx + 1) + ans[prev_idx] > s:
    #     s = h[i] * (i - prev_idx)
    s = h[i] * (i - prev_idx + 1) + ans[prev_idx]
    if max_wall <= h[i]:
        s += 1
        max_wall = h[i]
    ans.append(s)
    segment_tree.update(coordinate2idx[h[i]], i + 1)

print(*ans[1:])