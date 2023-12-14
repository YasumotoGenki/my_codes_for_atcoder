from collections import Counter
import heapq

n, q = map(int, input().split())
a = list(map(int, input().split()))

# A counter
a_counter = Counter(a)

# mex heapq and set
mex_heapq = []
heapq.heapify(mex_heapq)
count = 0
current_mex_candidate = 0
mex_set = set()
while(count < 4 * (10 ** 5) + 10):
    if current_mex_candidate not in a_counter:
        heapq.heappush(mex_heapq, current_mex_candidate)
        mex_set.add(current_mex_candidate)
        count += 1
    current_mex_candidate += 1

for _ in range(q):
    i, x = map(int, input().split())
    i -= 1
    a_counter[a[i]] -= 1
    if a_counter[a[i]] == 0:
        heapq.heappush(mex_heapq, a[i])
    a[i] = x
    if x not in a_counter:
        a_counter[x] = 1
    else:
        a_counter[x] += 1
    while(True):
        candidate = heapq.heappop(mex_heapq)
        if candidate in a_counter and a_counter[candidate] == 0:
            print(candidate)
            candidate
            heapq.heappush(mex_heapq, candidate)
            break
        if candidate not in a_counter:
            print(candidate)
            heapq.heappush(mex_heapq, candidate)
            break
