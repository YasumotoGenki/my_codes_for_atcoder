h, w = map(int, input().split())
s = []
mod = 998244353
for i in range(h):
    s.append(input())

# 連結成分を配列に格納
current_idx = 0
check_list = [[-1 for _ in range(w)] for _ in range(h)]
que = []
for h_idx in range(h):
    for w_idx in range(w):
        if check_list[h_idx][w_idx] == -1 and s[h_idx][w_idx] == "#":
            que.append([h_idx, w_idx])
        if que:
            while(que):
                cur_h_idx, cur_w_idx = que.pop()
                check_list[cur_h_idx][cur_w_idx] = current_idx
                if cur_h_idx - 1 >= 0 and check_list[cur_h_idx - 1][cur_w_idx] == -1 and s[cur_h_idx - 1][cur_w_idx] == "#":
                    que.append([cur_h_idx - 1, cur_w_idx])
                if cur_w_idx - 1 >= 0 and check_list[cur_h_idx][cur_w_idx - 1] == -1 and s[cur_h_idx][cur_w_idx - 1] == "#":
                    que.append([cur_h_idx, cur_w_idx - 1])
                if cur_h_idx + 1 < h and check_list[cur_h_idx + 1][cur_w_idx] == -1 and s[cur_h_idx + 1][cur_w_idx] == "#":
                    que.append([cur_h_idx + 1, cur_w_idx])
                if cur_w_idx + 1 < w and check_list[cur_h_idx][cur_w_idx + 1] == -1 and s[cur_h_idx][cur_w_idx + 1] == "#":
                    que.append([cur_h_idx, cur_w_idx + 1])
            current_idx += 1

base_count = current_idx
red_count = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            red_count += 1
green_count = h * w - red_count
ans = 0
# 赤マスを走査して、隣り合う緑の連結成分を確認
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            count = 0
            count_set= set()
            if i - 1 >= 0 and s[i - 1][j] == "#" and check_list[i - 1][j] not in count_set:
                count_set.add(check_list[i - 1][j])
                count += 1
            if j - 1 >= 0 and s[i][j - 1] == "#" and check_list[i][j - 1] not in count_set:
                count_set.add(check_list[i][j -1])
                count += 1
            if i + 1 < h and s[i + 1][j] == "#" and check_list[i + 1][j] not in count_set:
                count_set.add(check_list[i + 1][j])
                count += 1
            if j + 1  < w and s[i][j + 1] == "#" and check_list[i][j + 1] not in count_set:
                count_set.add(check_list[i][j + 1])
                count += 1
            count = count - 1
            
            ans += (current_idx - count)

class Modint:
    def __init__(self, value, mod):
        self.value = value % mod
        self.mod = mod

    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Modint):
            return self.value == other.value and self.mod == other.mod
        return False

    def __add__(self, other):
        other = self._to_modint(other)
        return Modint((self.value + other.value) % self.mod, self.mod)

    def __sub__(self, other):
        other = self._to_modint(other)
        return Modint((self.value - other.value) % self.mod, self.mod)

    def __mul__(self, other):
        other = self._to_modint(other)
        return Modint((self.value * other.value) % self.mod, self.mod)

    def __pow__(self, exponent):
        return Modint(pow(self.value, exponent, self.mod), self.mod)

    def __truediv__(self, other):
        other = self._to_modint(other)
        return self * other.inverse()

    def _to_modint(self, other):
        if isinstance(other, Modint) and self.mod == other.mod:
            return other
        elif isinstance(other, int):
            return Modint(other, self.mod)
        else:
            raise ValueError("Unsupported type for Modint operation")

    def inverse(self):
        # フェルマーの小定理を用いて逆元を計算
        # pow(a, -1, mod) は a の逆元を計算する Python の組み込み関数
        return Modint(pow(self.value, -1, self.mod), self.mod)

ans = Modint(ans, mod)

print(ans / Modint(red_count, mod))