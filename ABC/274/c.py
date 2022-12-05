n = int(input())
a = list(map(int, input().split()))

ans = [0]

for item_a in a:
    ans.append(ans[(item_a - 1)] + 1)
    ans.append(ans[(item_a - 1)] + 1)

for i in range(2 * n + 1):
    print(ans[i])
