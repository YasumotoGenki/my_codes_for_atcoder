n = int(input())
a = list(map(int, input().split()))

element2idx = dict()
for i in range(n):
    element2idx[a[i]] = i

ans = []
for i in range(n - 1):
    if a[i] != i + 1:
        idx = element2idx[i + 1]
        element2idx[a[i]] = idx
        a[idx] = a[i]
        a[i] = i + 1
        element2idx[i + 1] = i
        
        ans.append([i + 1, idx + 1])

print(len(ans))
for small, large in ans:
    print(small, large)