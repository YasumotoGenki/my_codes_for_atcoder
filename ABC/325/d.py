import heapq
n = int(input())
in_and_out_time = dict()
for i in range(n):
    t, d = map(int, input().split())
    if t in in_and_out_time:
        in_and_out_time[t].append(t + d)
    else:
        in_and_out_time[t] = [t + d]

idx = 0
key_length = len(in_and_out_time)
key_list = sorted(list(in_and_out_time.keys()))
que = []
heapq.heapify(que)
ans = 0
while(idx < key_length or que):
    if que:
        while(que):
            deadline = heapq.heappop(que)
            if deadline >= time:
                time += 1
                ans += 1
                break
    else:
        time = key_list[idx]
    if idx < key_length and time >= key_list[idx]:
        for item in in_and_out_time[key_list[idx]]:
            heapq.heappush(que, item)
        idx += 1
print(ans)