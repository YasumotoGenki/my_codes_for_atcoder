h, w = map(int, input().split())

a, b = [], []

for i in range(h):
    a.append(input())
for i in range(h):
    b.append(input())

for s in range(h):
    for t in range(w):
        corresponding_flg = True
        for h_i in range(h):
            for w_i in range(w):
                cur_h = h_i - s
                cur_w = w_i - t
                if a[cur_h][cur_w] == b[h_i][w_i]:
                    pass
                else:
                    corresponding_flg = False
        
        if corresponding_flg:
            print("Yes")
            exit()
print("No")