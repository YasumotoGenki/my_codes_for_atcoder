h, w = map(int, input().split())
square = []
for i in range(h):
    square.append(input())

visited = [[False for _ in range(w)] for _ in range(h)]
ans = 0
for h_idx in range(h):
    for w_idx in range(w):
        if square[h_idx][w_idx] == "#" and not visited[h_idx][w_idx]:
            que = [[h_idx, w_idx]]
            while(que):
                current_h_idx, current_w_idx = que.pop()
                visited[current_h_idx][current_w_idx] = True
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= current_h_idx + i <= h - 1 and 0 <= current_w_idx + j <= w - 1:
                            if square[current_h_idx + i][current_w_idx + j] == "#" and not visited[current_h_idx + i][current_w_idx +j]:
                                que.append([current_h_idx + i, current_w_idx + j])

            ans += 1
print(ans)