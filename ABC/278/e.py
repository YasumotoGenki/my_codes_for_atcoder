H, W, N, h, w = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

stack = [[[0 for _ in range(N + 1)] for _ in range(W + 1)] for __ in range(H + 1)]

for h_i in range(1, H + 1):
    for w_i in range(1, W + 1):
        for n in range(1, N + 1):
            stack[h_i][w_i][n] += stack[h_i - 1][w_i][n]
            stack[h_i][w_i][n] += stack[h_i][w_i - 1][n]
            stack[h_i][w_i][n] -= stack[h_i - 1][w_i - 1][n]
        stack[h_i][w_i][A[h_i - 1][w_i - 1]] += 1

for h_i in range(H - h + 1):
    ans = []
    for w_i in range(W - w + 1):
        cur_list = [0 for _ in range(N + 1)]
        count = 0
        for n in range(1, N + 1):
            cur_list[n] = stack[H][W][n]
            cur_list[n] -= stack[h_i + h][w_i + w][n]
            cur_list[n] += stack[h_i][w_i + w][n]
            cur_list[n] += stack[h_i + h][w_i][n]
            cur_list[n] -= stack[h_i][w_i][n]
            if cur_list[n] > 0:
                count += 1                
        ans.append(count)
    print(*ans)
