from itertools import permutations

h, w = map(int, input().split())
a, b = [], []
for i in range(h):
    a.append(list(map(int, input().split())))
for i in range(h):
    b.append(list(map(int, input().split())))

h_candidates = [i for i in range(h)]
w_candidates = [i for i in range(w)]
ans = 10 ** 10

for h_indices in permutations(h_candidates, h):
    for w_indices in permutations(w_candidates, w):
        candidate = [[] for _ in range(h)]
        for i, h_idx in enumerate(h_indices):
            for j, w_idx in enumerate(w_indices):
                candidate[i].append(b[h_idx][w_idx])
        flg = True
        for i in range(h):
            for j in range(w):
                if a[i][j] == candidate[i][j]:
                    pass
                else:
                    flg = False
                    break
        if flg:
            h_candidates_indices = list(h_indices)
            w_candidates_indices = list(w_indices)
            count = 0
            for i in range(h):
                idx = h_candidates_indices.index(i)
                for j in range(idx, i, -1):
                    h_candidates_indices[j - 1], h_candidates_indices[j] = h_candidates_indices[j], h_candidates_indices[j - 1]
                count += idx - i
            for i in range(w):
                idx = w_candidates_indices.index(i)
                for j in range(idx, i, -1):
                    w_candidates_indices[j - 1], w_candidates_indices[j] = w_candidates_indices[j], w_candidates_indices[j - 1]
                count += idx - i
            ans = min(ans, count)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)