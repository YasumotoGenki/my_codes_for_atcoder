n = int(input())
s = []
for i in range(n):
    s.append(input())
indices = [i for i in range(n)]
s, indices = zip(*sorted(zip(s, indices)))

ans = [0] * n
for i in range(n - 1):
    count = 0
    for j in range(min(len(s[i]), len(s[i + 1]))):
        if s[i][j] == s[i + 1][j]:
            count += 1
        else:
            break
    idx = indices[i]
    ans[idx] = max(ans[idx], count)
    idx = indices[i + 1]
    ans[idx] = max(ans[idx], count)
        
for i in range(n):
    print(ans[i])