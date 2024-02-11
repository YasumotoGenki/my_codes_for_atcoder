import heapq

n = int(input())
INF = 10 ** 100
dp = [INF for _ in range(n)]
dp[0] = 0
abx  = []
for i in range(n - 1):
    abx.append(list(map(int, input().split())))

que = [[0, 0]] # [cost, node]
heapq.heapify(que)
while(que):
    cost, current_stage = heapq.heappop(que)
    if cost > dp[-1]:
        break
    a, b, x = abx[current_stage]
    if dp[current_stage + 1] > dp[current_stage] + a:
        dp[current_stage + 1] = dp[current_stage] + a
        if current_stage + 1 < n - 1:
            heapq.heappush(que, [dp[current_stage + 1], current_stage + 1])
    if dp[x - 1] > dp[current_stage] + b:
        dp[x - 1] = dp[current_stage] + b
        if x - 1 < n - 1:
            heapq.heappush(que, [dp[x - 1], x - 1])
            # que.append(x - 1)

print(dp[-1])