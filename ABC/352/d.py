import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
num2idx_dict = dict()

for i in range(n):
    num2idx_dict[p[i]] = i

min_idx_heapq = []
max_idx_heapq = []
max_idx = 0
min_idx = n

for i in range(k):
    heapq.heappush(min_idx_heapq, num2idx_dict[i + 1])
    heapq.heappush(max_idx_heapq, -num2idx_dict[i + 1])
    if min_idx > num2idx_dict[i + 1]:
        min_idx = num2idx_dict[i + 1]
    if max_idx < num2idx_dict[i + 1]:
        max_idx = num2idx_dict[i + 1]

ans = n

for i in range(n - k + 1):
    if i != 0:
        heapq.heappush(min_idx_heapq, num2idx_dict[i + k])
        heapq.heappush(max_idx_heapq, -num2idx_dict[i + k])
        while(True):
            min_idx = heapq.heappop(min_idx_heapq)
            if p[min_idx] < i + 1 or p[min_idx] > i + k:
                continue
            else:
                heapq.heappush(min_idx_heapq, min_idx)
                break
        while(True):
            max_idx = heapq.heappop(max_idx_heapq)
            max_idx = -max_idx
            if p[max_idx] < i + 1 or p[max_idx] > i + k:
                continue
            else:
                heapq.heappush(max_idx_heapq, -max_idx)
                break
    ans = min(ans, max_idx - min_idx)

print(ans)