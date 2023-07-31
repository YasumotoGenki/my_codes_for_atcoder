n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

for h in range(n - 9 + 1):
    for w in range(m - 9 + 1):
        flg = True
        for i in range(4):
            for j in range(4):
                if i == 3 or j == 3:
                    if s[h + i][w + j] != ".":
                        flg = False
                elif s[h + i][w + j] != "#":
                    flg = False
        for i in range(5, 9):
            for j in range(5, 9):
                if i == 5 or j == 5:
                    if s[h + i][w + j] != ".":
                        flg = False
                elif s[h + i][w + j] != "#":
                    flg = False
        if flg:
            print(h + 1, w + 1)