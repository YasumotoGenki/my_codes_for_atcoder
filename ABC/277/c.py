n = int(input())
radder_dict = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a in radder_dict:
        radder_dict[a].append(b)
    else:
        radder_dict[a] = [b]
    if b in radder_dict:
        radder_dict[b].append(a)
    else:
        radder_dict[b] = [a]
ans = 1
que = [1]
done_set = set()
done_set.add(1)

while(que):
    cur = que.pop()
    if cur in radder_dict:
        for next_floor in radder_dict[cur]:
            if next_floor not in done_set:
                que.append(next_floor)
                ans = max(ans, next_floor)
                done_set.add(next_floor)
print(ans)