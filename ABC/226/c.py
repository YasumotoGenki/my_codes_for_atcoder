n = int(input())
parent = [[] for _ in range(n)]
t = [0 for _ in range(n)]
for i in range(n):
    input_list = list(map(int, input().split()))
    t[i] = input_list[0]
    if input_list[1] > 0:
        parent[i] = input_list[2:]
que = []
que.append(n - 1)
ans = 0
done_set = set()
while(que):
    p_idx = que.pop()
    ans += t[p_idx]
    done_set.add(p_idx)
    for item in parent[p_idx]:
        item -= 1
        if item not in done_set:
            que.append(item)
            done_set.add(item)
print(ans)