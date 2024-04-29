h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

def check_magnet(cur_h, cur_w):
    global s
    global h
    global w
    if cur_h > 0 and s[cur_h - 1][cur_w] == "#":
        return True
    if cur_h < h - 1 and s[cur_h + 1][cur_w] =="#":
        return True
    if cur_w > 0 and s[cur_h][cur_w - 1] == "#":
        return True
    if cur_w < w - 1 and s[cur_h][cur_w  +  1]=="#":
        return True
    return False 

field = [[set() for _ in range(w)] for _ in range(h)]
group_idx = 0
ans = 0
count = 0

for i in range(h):
    for j in range(w):
        ans = max(count, ans)
        count =  0
        group_idx += 1
        if s[i][j] == "#":
            continue
        if check_magnet(i,j):
            count = 1
            field[i][j].add(group_idx)
            continue

        if len(field[i][j]) == 0:
            # dfs
            count = 1
            que = [[i, j]]
            while(que):
                cur_h, cur_w = que.pop()
                field[cur_h][cur_w].add(group_idx)
                for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= cur_h + dx <= h - 1 and 0 <= cur_w + dy <= w - 1 and group_idx not in field[cur_h + dx][cur_w + dy]:
                        if s[cur_h][cur_w] == "#":
                            continue
                        if check_magnet(cur_h + dx, cur_w + dy):
                            pass
                        else:
                            que.append([cur_h + dx, cur_w + dy])
                        field[cur_h + dx][cur_w + dy].add(group_idx)
                        count += 1

ans = max(count, ans)
print(ans)