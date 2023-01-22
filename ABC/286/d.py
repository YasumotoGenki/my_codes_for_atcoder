n, x = map(int, input().split())
ab = dict()
for i in range(n):
    a, b = map(int, input().split())
    ab[a] = b

dp = [False] * 107101
dp[0] = True

for a, b in ab.items():
    stack = []
    for i in range(1, b + 1):
        stack.append(i * a)
    for i in range(len(dp) - 1, -1, -1):
        for s in stack:
            if i + s < len(dp) and dp[i]:
                dp[i + s] = True
if dp[x]:
    print("Yes")
else:
    print("No")