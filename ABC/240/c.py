import copy

n, x = map(int, input().split())
list_a, list_b = [], []
for i in range(n):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

dp = [False for _ in range(x + 1)]
# if list_a[0] <= x:
#     dp[list_a[0]] = True
# if list_b[0] <= x:
#     dp[list_b[0]] = True
dp[0] = True

for i in range(n):
    new_dp = [False for _ in range(x + 1)]
    for j in range(x):
        if i < n - 1 and dp[j]:
            if list_a[i] + j <= x:
                new_dp[list_a[i] + j] = True
            if list_b[i] + j <= x:
                new_dp[list_b[i] + j] = True
        if i == n - 1 and dp[j]:
            if list_a[i] + j == x:
                print("Yes")
                exit()
            if list_b[i] + j == x:
                print("Yes")
                exit()
    dp = copy.deepcopy(new_dp)
print("No")