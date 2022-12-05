h, m = map(str, input().split())
h = h.zfill(2)
m = m.zfill(2)

flg = True
while(flg):
    if int(h[0] + m[0]) <= 23 and int(h[1] + m[1]) <= 59:
        ans = h + " " + m
        flg = False
    else:
        if int(m) + 1 <= 59:
            m = str(int(m) + 1).zfill(2)
        else:
            m ='00'
            if int(h) + 1 <= 23:
                h = str(int(h) + 1).zfill(2)
            else:
                h = '00'
print(ans)