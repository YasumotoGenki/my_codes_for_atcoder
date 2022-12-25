class BIT():
    def __init__(self, num) -> None:
        self.n = num
        self.tree = [set()] * (num + 1)

    def search(self, i):
        s = set()
        i = self.n - i
        while i > 0:
            s |= (self.tree[i])
            i -= i & -i
        return s

    def add(self, i, x):
        i = self.n - i
        while i <= self.n:
            self.tree[i].add(x)
            i += i & -i

s = input()
length_s = len(s)
count = 0
stack = set()
bit = BIT(length_s // 2 + 1)
box = set()

for i in range(length_s):
    if s[i] == "(":
        count += 1
    elif s[i] == ")":
        count -= 1
        box = box - bit.search(count)
    else:
        if s[i] in box:
            print("No")
            exit()
        bit.add(count, s[i])
        box.add(s[i])
print("Yes")