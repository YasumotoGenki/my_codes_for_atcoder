H, W, C, Q = map(int, input().split())

q_list = []
h_q_list, w_q_list = [], []
h_q_dict, w_q_dict = dict(), dict()
h_idx, w_idx = 0, 0
# dup_list = []
# dup_list.append([0, 0])
ans = [0 for i in range(C)]

for i in range(Q):
    t, n, c = map(int, input().split())
    q_list.append([t, n, c])
    if t == 1:
        w_idx += 1
        w_q_list.append([i, n, c, w_idx, h_idx])
        if n in w_q_dict:
            w_q_dict[n] = [i, len(w_q_list)]
            # a, b = dup_list[-1]
            # dup_list.append([a, b + 1])
        else:
            w_q_dict[n] = [i, len(w_q_list)]
            # a, b = dup_list[-1]
            # dup_list.append([a, b])
    else:
        h_idx += 1
        h_q_list.append([i, n, c, w_idx, h_idx])
        if n in h_q_dict:
            # a, b = dup_list[-1]
            # dup_list.append([a + 1, b])
            h_q_dict[n] = [i, len(h_q_list)]
        else:
            # a, b = dup_list[-1]
            # dup_list.append([a, b])
            h_q_dict[n] = [i, len(h_q_list)]

w_set = set()
h_set = set()
future_list = []
future_list.append([0, 0])

for i in range(Q - 1, -1, -1):
    t, n, c = q_list[i]
    if t == 1:
        w_set.add(n)
        wc, hc = future_list[-1]
        future_list.append([len(w_set), hc])
    else:
        h_set.add(n)
        wc, hc = future_list[-1]
        future_list.append([wc, len(h_set)])

for i, n, c, w_idx, h_idx in h_q_list:
    if i != h_q_dict[n][0]:
        continue
    ans[c - 1] += H - future_list[Q - i][0] # (len(w_q_list) - w_idx) + 

for i, n, c, w_idx, h_idx in w_q_list:
    if i != w_q_dict[n][0]:
        continue
    ans[c - 1] += W - future_list[Q - i][1] #(len(h_q_list) - h_idx) + (dup_list[-1][0] - dup_list[i + 1][0])

print(*ans)
