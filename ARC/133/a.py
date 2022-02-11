n = int(input())
a = list(map(int, input().split()))

set_num = set(a)
if len(set_num) == 1:
    print()
    exit()
else:
    pre_num = a[0]
    for i in range(1, n):
        if pre_num > a[i]:
            pop_num = pre_num
            break
        pre_num = a[i]
    else:
        pop_num = a[-1]
    for i in range(n - 1, -1, -1):
        if a[i] == pop_num:
            a.pop(i)
    print(*a)