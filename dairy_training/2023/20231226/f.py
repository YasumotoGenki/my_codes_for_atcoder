import heapq

n = int(input())
a = list(map(int, input().split()))

odd, even = [], []
heapq.heapify(odd)
heapq.heapify(even)

for item in a:
    if item % 2 == 0:
        heapq.heappush(even, -item)
    else:
        heapq.heappush(odd, -item)

ans = -1
if len(even) >= 2:
    num_1 = heapq.heappop(even)
    num_2 = heapq.heappop(even)
    ans = max(ans, abs(num_1 + num_2))
if len(odd) >= 2:
    num_1 = heapq.heappop(odd)
    num_2 = heapq.heappop(odd)
    ans = max(ans, abs(num_1 + num_2))

print(ans)