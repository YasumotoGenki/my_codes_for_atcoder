from collections import defaultdict as ddict
N = int(input())
S = ddict(int)
for i in range(N):
    s = input()
    S[s] += 1

ans = sorted(S.items(), reverse=True, key=lambda x: x[1])[0][0]
print(ans)