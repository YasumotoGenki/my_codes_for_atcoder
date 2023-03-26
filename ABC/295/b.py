r, c = map(int, input().split())
b = []
new_map = [["." for _ in range(c)] for _ in range(r)]
for idx_r in range(r):
    b.append(input())
    for idx_c in range(c):
        if b[idx_r][idx_c] == "#":
            new_map[idx_r][idx_c] = "#"

for idx_r in range(r):
    for idx_c in range(c):
        if b[idx_r][idx_c] != "." and b[idx_r][idx_c] != "#":
            bomb_num = int(b[idx_r][idx_c])
            for idx_new_map_r in range(r):
                for idx_new_map_c in range(c):
                    if abs(idx_new_map_r - idx_r) + abs(idx_new_map_c - idx_c) <= bomb_num:
                        new_map[idx_new_map_r][idx_new_map_c] = "."

for idx_r in range(r):
    print("".join(new_map[idx_r]))