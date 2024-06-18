n, m, k = map(int, input().split())

cases = []
for _ in range(m):
    cases.append(list(map(str, input().split())))

ans = 0
for i in range(1 << n):
    flg = True
    for j in range(m):
        case = cases[j]
        judge = case[-1]
        c = int(case[0])
        a = list(map(int, case[1:c + 1]))
        count = 0
        for item_a in a:
            power = item_a - 1
            if i & 1 << power:
                count += 1
        if judge == "o":
            if count < k:
                flg = False
                break
        else:
            if count >= k:
                flg = False
                break
    if flg:
        ans += 1

print(ans)
