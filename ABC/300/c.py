h, w = map(int, input().split())
c = []
for i in range(h):
    c.append(input())

ans = [0 for _ in range(min(h, w))]

for h_i in range(1, h - 1):
    for w_i in range(1, w - 1):
        if c[h_i][w_i] == "#":
            count = 0
            flg = True
            while(flg):
                if h_i - count - 1 < 0 or w_i - count - 1 < 0 or c[h_i - count - 1][w_i - count - 1] == ".":
                    break
                if h_i - count - 1 < 0 or w_i + count + 1 > w - 1 or c[h_i - count - 1][w_i + count + 1] == ".":
                    break
                if h_i + count + 1 > h - 1 or w_i - count - 1 < 0 or c[h_i + count + 1][w_i - count - 1] == ".":
                    break
                if h_i + count + 1 > h - 1 or w_i + count + 1 > w - 1 or c[h_i + count + 1][w_i + count + 1] == ".":
                    break
                count += 1
            if count > 0:
                ans[count - 1] += 1

for i in range(len(ans)):
    ans[i] = str(ans[i])
print(" ".join(ans))
