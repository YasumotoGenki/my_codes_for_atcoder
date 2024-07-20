import heapq

n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

boxes = [[] for _ in range(n)]

for i in range(n):
    heapq.heappush(boxes[a[i] - 1], w[i])

ans = 0
for i in range(n):
    while(len(boxes[i]) > 1):
        item = heapq.heappop(boxes[i])
        ans += item

print(ans)
