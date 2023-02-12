n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

# 1 -> can be reached
# 0 -> not be reached yet
# -1 -> cannot be reached
dp = [0 for _ in range(x + 1)]
for i in range(m):
    dp[b[i]] = -1
dp[0] = 1

for i in range(x - 1):
    if dp[i] == 1:
        for j in range(n):
            next_step = i + a[j]
            if next_step < x + 1 and dp[next_step] != -1:
                dp[next_step] = 1
if dp[-1] == 1:
    print("Yes")
else:
    print("No")
