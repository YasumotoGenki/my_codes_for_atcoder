h, w, n = map(int, input().split())
t = input()
s = []
for i in range(h):
    s.append(input())

ans = 0
for start_h_idx in range(1, h - 1):
    for start_w_idx in range(1, w - 1):
        current_h = start_h_idx
        current_w = start_w_idx
        if s[current_h][current_w] == "#":
            continue
        flg = True
        for i in range(n):
            if t[i] == "L":
                current_w -= 1
            elif t[i] == "R":
                current_w += 1
            elif t[i] == "U":
                current_h -= 1
            elif t[i] == "D":
                current_h += 1
            if s[current_h][current_w] == "#":
                flg = False
                break
        if flg:
            ans += 1

print(ans)
