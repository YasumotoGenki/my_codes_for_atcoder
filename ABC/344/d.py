from copy import deepcopy

t = input()
n = int(input())
s_list = []
for i in range(n):
    input_list = list(map(str, input().split()))
    a, s = input_list[0], input_list[1:]
    s_list.append(s)

dp = [-1 for  _ in range(len(t) + 1)]
dp[0] = 0

t_length = len(t)
for i in range(n):
    previous_dp = deepcopy(dp)
    for item in s_list[i]:
        for j in range(len(t) - 1, -1, -1):
            item_length = len(item)
            if j + item_length <= t_length and item == t[j:j + item_length] and previous_dp[j] != -1:
                if previous_dp[j + item_length] == -1:
                    dp[j + item_length] = previous_dp[j] + 1
                else:
                    dp[j + item_length] = min(dp[j + item_length], previous_dp[j] + 1)

print(dp[-1])
