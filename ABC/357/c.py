n = int(input())

dp = []
for i in range(n + 1):
    if i == 0:
        dp.append([["#"]])
        continue
    cur = [["" for _ in range(3 ** i)] for _ in range(3 ** i)]
    for h in range(3 ** i):
        for w in range(3 ** i):
            if 3 ** (i - 1) <= h < 3 ** (i - 1) + 3 ** (i - 1) and 3 ** (i - 1) <= w < 3 ** (i - 1) + 3 ** (i - 1):
                cur[h][w] = "."
                continue
            cur[h][w] = dp[-1][h % (3 ** (i - 1))][w % (3 ** (i - 1))]
    dp.append(cur)

for i in range(3 ** n):
    print("".join(dp[-1][i]))