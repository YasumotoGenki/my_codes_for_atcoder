s_list = []
for i in range(9):
    s_list.append(input())

ans = []
for i in range(9):
    for j in range(9):
        if s_list[i][j] == "#":
            for h in range(9):
                for w in range(9):
                    current_points = [[i, j], [h, w]]
                    if i == h and j == w:
                        continue
                    if s_list[h][w] != "#":
                        continue
                    diff_h = h - i
                    diff_w = w - j
                    next_h = h + diff_w
                    next_w = w - diff_h
                    if 0 <= next_h < 9 and 0 <= next_w < 9 and s_list[next_h][next_w] == "#" and [next_h, next_w] not in current_points:
                        current_points += [[next_h, next_w]]
                    else:
                        continue
                    next_h = next_h - diff_h
                    next_w = next_w - diff_w
                    if 0 <= next_h < 9 and 0 <= next_w < 9 and s_list[next_h][next_w] == "#" and [next_h, next_w] not in current_points:
                        current_points += [[next_h, next_w]]
                        current_points.sort()
                        if current_points not in ans:
                            ans.append(current_points)
print(len(ans))