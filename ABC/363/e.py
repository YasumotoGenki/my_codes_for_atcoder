h, w, y = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))

que = [[] for _ in range(y + 1)]
qued_list = [[False for _ in range(w)] for _ in range(h)]
total = h * w
drop_count = 0

for h_idx in range(h):
    qued_list[h_idx][0] = True
    if a[h_idx][0] <= y:
        que[a[h_idx][0]].append([h_idx, 0])
        
    if not qued_list[h_idx][w - 1]:
        qued_list[h_idx][w - 1] = True
        if a[h_idx][w - 1] <= y:
            que[a[h_idx][w - 1]].append([h_idx, w - 1])

for w_idx in range(w):
    if w_idx != 0 and w_idx != w - 1:
        qued_list[0][w_idx] = True
        if not qued_list[0][w_idx] and a[0][w_idx] <= y:
            que[a[0][w_idx]].append([0, w_idx])
        if not qued_list[h - 1][w_idx]:
            qued_list[h - 1][w_idx] = True
            if a[h - 1][w_idx] <= y:
                que[a[h - 1][w_idx]].append([h - 1, w_idx])


for year in range(1,  y + 1):
    idx = 0
    while(len(que[year]) > idx):
        h_idx, w_idx = que[year][idx]
        drop_count += 1
        idx += 1
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            if 0 <= h_idx + dx <= h - 1 and 0 <= w_idx + dy <= w - 1:
                if not qued_list[h_idx + dx][w_idx + dy]:
                    qued_list[h_idx + dx][w_idx + dy] = True
                    if a[h_idx + dx][w_idx + dy] <= year:
                        que[year].append([h_idx + dx, w_idx + dy])
                    elif a[h_idx + dx][w_idx + dy] <= y:
                        que[a[h_idx + dx][w_idx + dy]].append([h_idx + dx, w_idx + dy])
    print(total - drop_count)