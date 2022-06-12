import heapq

q = int(input())
s = dict()

min_que, max_que = [], []
heapq.heapify(min_que)
heapq.heapify(max_que)

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        if x not in s:
            s[x] = 1
            heapq.heappush(min_que, x)
            heapq.heappush(max_que, -x)
        else:
            if s[x] == 0:
                heapq.heappush(min_que, x)
                heapq.heappush(max_que, -x)
            s[x] += 1
    elif query[0] == 2:
        x, c = query[1], query[2]
        if x not in s:
            continue
        s[x] -= min(c, s[x])
    else:
        min_v, max_v = 0, 0
        while(min_v == 0):
            min_v = heapq.heappop(min_que)
            if min_v not in s or s[min_v] == 0:
                min_v = 0
        while(max_v == 0):
            max_v = heapq.heappop(max_que)
            max_v = -max_v
            if max_v not in s or s[max_v] == 0:
                max_v = 0
        print(max_v - min_v)
        heapq.heappush(min_que, min_v)
        heapq.heappush(max_que, -max_v)