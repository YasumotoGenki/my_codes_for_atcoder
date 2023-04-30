import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 既出の集合
alreadly_confirmed_num_set = set()
# heapq
hq = []
ans = []

for i in range(n):
    if a[i] not in alreadly_confirmed_num_set:
        heapq.heappush(hq, a[i])
    alreadly_confirmed_num_set.add(a[i])

while(len(ans) < k):
    # heapqから最小のものを取り出す -> ansに追加
    cur_sum_value = heapq.heappop(hq)
    ans.append(cur_sum_value)
    
    # もう一つ買った場合を考える
    for i in range(n):
        if cur_sum_value + a[i] not in alreadly_confirmed_num_set:
            heapq.heappush(hq, cur_sum_value + a[i])
            alreadly_confirmed_num_set.add(cur_sum_value + a[i])

print(ans[-1])