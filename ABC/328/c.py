n, q = map(int, input().split())
s = input()
cumulative_sum = [0]
for i in range(n - 1):
    if s[i] == s[i + 1]:
        cumulative_sum.append(cumulative_sum[-1] + 1)
    else:
        cumulative_sum.append(cumulative_sum[-1])

for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(cumulative_sum[r] - cumulative_sum[l])
