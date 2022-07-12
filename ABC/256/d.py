n = int(input())
lr = [-1 for i in range(2 * 100000 + 1)]
for i in range(n):
    l, r = map(int, input().split())
    while(l < r):
        if lr[l] == -1:
            lr[l] = r
            l += 1
        else:
            if r > lr[l]:
                for j in range(lr[l], r):
                    if lr[j] >= r:
                        break
                    lr[j] = r
                l = r
            else: # r <= lr[l]
                l = r


flg = False
pre_num = 10000000
for i in range(1, 2 * 100000 + 1):
    if lr[i] != -1:
        flg = True
        pre_num = min(pre_num, i)
    else:
        if flg:
            print(pre_num, i)
            pre_num = 10000000
            flg = False