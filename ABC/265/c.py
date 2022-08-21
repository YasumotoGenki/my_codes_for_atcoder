h, w = map(int, input().split())
g = []
for i in range(h):
    g.append(input())

done = [[False for _ in range(w)] for __ in range(h)]
h_idx, w_idx = 0, 0
while(True):
    if done[h_idx][w_idx]:
        print(-1)
        exit()
    else:
        done[h_idx][w_idx] = True

    cur = g[h_idx][w_idx]    
    if cur == 'U' and h_idx > 0:
        h_idx -= 1
    elif cur == 'D' and h_idx < h - 1:
        h_idx += 1
    elif cur == 'L' and w_idx > 0:
        w_idx -= 1
    elif cur == 'R' and w_idx < w - 1:
        w_idx += 1
    else:
        h_idx += 1
        w_idx += 1
        print(h_idx, w_idx)
        exit()