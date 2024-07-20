n = int(input())

max_value = 0
min_value = 0

lr = []

for _ in range(n):
    l, r = map(int, input().split())
    min_value += l
    max_value += r
    lr.append([l, r])

if min_value <= 0 <= max_value:
    remained = -min_value
    print("Yes")
    ans = []
    for i in range(n):
        l, r = lr[i]
        diff = r - l
        if remained > 0:
            if diff <= remained:
                ans.append(r)
                remained -= diff
            else:
                ans.append(l + remained)
                remained = 0
        else:
            ans.append(l)
    print(*ans)
    # print(sum(ans))
else:
    print("No")