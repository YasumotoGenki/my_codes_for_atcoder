n = int(input())

xy = []
xy_to_idx_dict = dict()
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])
    xy_to_idx_dict[str(x) + '|' + str(y)] = i

kind_list = [-1] * n
count = 1
for i in range(n):
    if kind_list[i] != -1:
        continue
    kind_list[i] = count
    que = [i]
    while(que):
        idx = que.pop()
        x, y = xy[idx]
        for x_idx in range(-1, 2):
            for y_idx in range(-1, 2):
                if x_idx == 0 and y_idx == 0:
                    continue
                if x_idx == -1 and y_idx == 1:
                    continue
                if x_idx == 1 and y_idx == -1:
                    continue
                if -1000 <= x + x_idx <= 1000 and -1000 <= y + y_idx <= 1000 and str(x + x_idx) + "|" + str(y + y_idx) in xy_to_idx_dict:
                    next_idx = xy_to_idx_dict[str(x + x_idx) + "|" + str(y + y_idx)]
                    if kind_list[next_idx] == -1:
                        que.append(next_idx)
                        kind_list[next_idx] = count
    count += 1

print(max(kind_list))