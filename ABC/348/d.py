from collections import deque
import heapq

h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(input())

n = int(input())
drug_map = []
for _ in range(h):
    drug_map.append([0 for _ in range(w)])

for _ in range(n):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    drug_map[r][c] = e

state_map = []
for _ in range(h):
    state_map.append([-1 for _ in range(w)])

for h_idx in range(h):
    for w_idx in range(w):
        if a[h_idx][w_idx] == "S":
            start_h, start_w = h_idx, w_idx
        if a[h_idx][w_idx] == "T":
            end_h, end_w = h_idx, w_idx

que = []
heapq.heapify(que)
heapq.heappush(que, [0, start_h, start_w])

def dfs():
    global drug_map
    global a
    global state_map
    global que

    # 現在状況
    energy, current_h, current_w = heapq.heappop(que)
    energy = - energy

    # 薬を使うかどうか
    if drug_map[current_h][current_w] > energy and state_map[current_h][current_w] < drug_map[current_h][current_w]:
        energy = drug_map[current_h][current_w]
        state_map[current_h][current_w] = energy
        drug_map[current_h][current_w] = 0

    if current_h == end_h and current_w == end_w:
        print("Yes")
        exit()

    # 上下左右
    if energy > 0:
        for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if h > current_h + x >= 0 and w > current_w + y >= 0 and a[current_h + x][current_w + y] != "#":
                if state_map[current_h + x][current_w + y] < energy - 1:
                    state_map[current_h + x][current_w + y] = energy - 1
                    # que.append([1 - energy, current_h + x, current_w + y])
                    heapq.heappush(que, [1 - energy, current_h + x, current_w + y])

    if len(que) == 0:
        print("No")
        exit()

while(True):
    dfs()