h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

for h_idx in range(h):
    for w_idx in range(w - 1):
        if s[h_idx][w_idx] == 'T' and s[h_idx][w_idx + 1] == 'T':
            s[h_idx][w_idx] = 'P'
            s[h_idx][w_idx + 1] = 'C'

for i in range(h):
    print("".join(s[i]))
