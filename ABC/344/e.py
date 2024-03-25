n = int(input())
a = list(map(int, input().split()))
q = int(input())

previous_num = None
# dict {x: [1つ前の要素、1つ後の要素]}
renketu_dict = dict()

for i, item_a in enumerate(a):
    if i == n - 1:
        renketu_dict[item_a] = [previous_num, None]
    else:
        renketu_dict[item_a] = [previous_num, a[i + 1]]
        previous_num = item_a

start = a[0]

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1], query[2]
        prev_num, next_num = renketu_dict[x]
        renketu_dict[y] = [x, next_num]
        renketu_dict[x] = [prev_num, y]
        if next_num is not None:
            renketu_dict[next_num] = [y, renketu_dict[next_num][1]]
    else:
        x = query[1]
        prev_num, post_num = renketu_dict[x]
        if prev_num is None:
            start = post_num
            renketu_dict[post_num] = [None, renketu_dict[post_num][1]]
        else:
            renketu_dict[prev_num] = [renketu_dict[prev_num][0], post_num]
        if post_num is None:
            renketu_dict[prev_num] = [renketu_dict[prev_num][0], None]
        else:
            renketu_dict[post_num] = [prev_num, renketu_dict[post_num][1]]
        renketu_dict.pop(x)

ans = []
que = [start]
while(que):
    current = que.pop()
    ans.append(str(current))
    if renketu_dict[current][1] is None:
        break
    else:
        que.append(renketu_dict[current][1])

print(" ".join(ans))