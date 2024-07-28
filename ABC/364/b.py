h, w = map(int, input().split())
si, sj = map(int, input().split())
si -= 1
sj -= 1

c = []
for i in range(h):
    c.append(list(input()))
x = input()

h_idx = si
w_idx = sj

for i in range(len(x)):
    if x[i] == "L":
        if w_idx > 0 and c[h_idx][w_idx - 1] == ".":
            w_idx -= 1
    elif x[i] == "R":
        if w_idx < w - 1 and c[h_idx][w_idx + 1] == ".":
            w_idx += 1
    elif x[i] == "U":
        if h_idx > 0 and c[h_idx - 1][w_idx] == ".":
            h_idx -= 1
    else:
        if h_idx < h - 1 and c[h_idx + 1][w_idx] == ".":
            h_idx += 1

print(h_idx + 1, w_idx + 1)