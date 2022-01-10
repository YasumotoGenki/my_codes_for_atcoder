H, W = map(int, input().split())
C = []
for i in range(H):
    c = input()
    C.append(c)

que = [[0, 0]]
done_list = [[False for _ in range(W)] for i in range(H)]
ans = 0

while(que):
    h, w = que.pop()
    if h + 1 < H and not done_list[h + 1][w] and C[h + 1][w] != "#":
        que.append([h + 1, w])
        done_list[h + 1][w] = True
    if w + 1 < W and not done_list[h][w + 1] and C[h][w + 1] != "#":
        que.append([h, w + 1])
        done_list[h][w + 1] = True
    ans = max(ans, h + w + 1)

print(ans)