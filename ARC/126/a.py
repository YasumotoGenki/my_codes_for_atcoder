t = int(input())
for i in range(t):
    ans = 0
    n2, n3, n4 = map(int, input().split())
    if n3 > 0:
        num = n3 // 2
        if n4 > 0:
            if n4 >= num:
                ans += num
                n4 -= num
                num = 0
            else:
                ans += n4
                num -= n4
                n4 = 0
        if num > 0 and n2 > 0:
            if n2 // 2 >= num:
                ans += num
                n2 -= 2 * num
            else:
                ans += n2 // 2
                n2 = n2 % 2
    if n4 > 0:
        num = n4 // 2
        rem = n4 % 2
        if num > 0 and n2 > 0:
            if n2 >= num:
                ans += num
                n2 -= num
            else:
                ans += n2
                n2 = 0
                print(ans)
                continue
        if rem > 0 and n2 >= 3:
            ans += 1
            n2 -= 3
    if n2 > 0:
        ans += n2 // 5
    print(ans)

