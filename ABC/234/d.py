import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
pre_num = 0

hq = []

for i in range(n):
    element = p[i]
    heapq.heappush(hq, element)
    if i > k - 1:
        heapq.heappop(hq)
    if i >= k - 1:
        ans = heapq.heappop(hq)
        print(ans)
        heapq.heappush(hq, ans)
        
