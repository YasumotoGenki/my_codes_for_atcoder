n = int(input())
a = list(map(int, input().split()))

pre_num = 0
pre_count = 0
s = []
ans = 0

for i in range(n):
    if i == 0 or len(s) == 0:
        ans += 1
        print(ans)
        s.append(a[i])
        pre_num = a[i]
        pre_count += 1
    else:
        ans += 1
        if pre_num == a[i]:
            pre_count += 1
            s.append(a[i])
            if pre_count == pre_num:
                ans -= pre_num
                pre_count = 0
                for i in range(pre_num):
                    s.pop()
                if s:
                    pre_num = s[-1]
                    pre_count = 1
                    idx = -2
                    while(abs(idx) <= len(s) and s[idx] == pre_num):
                        pre_count += 1
                        idx -= 1
                else:
                    pre_num = 0
                    pre_count = 0
        else:
            pre_count = 1
            pre_num = a[i]
            s.append(a[i])
        print(ans)
            