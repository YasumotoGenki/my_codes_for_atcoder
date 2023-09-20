import heapq
from bisect import bisect_left

n, m = map(int, input().split())
list_t = []
list_w = []
list_s = []
for  _ in range(m):
    t, w, s = map(int, input().split())
    list_t.append(t)
    list_s.append(s)
    list_w.append(w)

waiting_list = [i for i in range(n)]
heapq.heapify(waiting_list)
comeback_people_dict = dict()

waiting_people_count = n
ans = [0 for _ in range(n)]

for i in range(m):
    t = list_t[i]
    if t in comeback_people_dict:
        for person in comeback_people_dict[t]:
            heapq.heappush(waiting_list, person)
            waiting_people_count += 1
    if waiting_people_count > 0:
        eating_person = heapq.heappop(waiting_list)
        waiting_people_count -= 1
        ans[eating_person] += list_w[i]
        if t + list_s[i] <= list_t[-1]:
            tidx = bisect_left(list_t, t + list_s[i])
            next_t = list_t[tidx]
            if next_t in comeback_people_dict:
                comeback_people_dict[next_t].append(eating_person)
            else:
                comeback_people_dict[next_t] = [eating_person]
    else:
        pass
for i in range(n):
    print(ans[i])