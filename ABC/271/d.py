n, s = map(int, input().split())
a_list, b_list = [], []
for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

dp = [[None for _ in range(s + 1)] for __ in range(n + 1)]

dp[0][0] = ''
for i in range(n):
    for j in range(s + 1):
        if dp[i][j] != None:
            if j + a_list[i] <= s:
                dp[i + 1][j + a_list[i]] = dp[i][j] + 'H'
            if j + b_list[i] <= s:
                dp[i + 1][j + b_list[i]] = dp[i][j] + 'T'
if dp[-1][-1] != None:
    print("Yes")
    print(dp[-1][-1])
else:
    print("No")